"""
!!!! IMPORTANT !!!!
 - procuct means blog 
 - example procust_title is simpli a title of blog
"""


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

from .models import Blog, FavoriteProduct
from .forms import CreateUserForm, BlogForm
from .decorators import unauthenticated_page_for_logged_user, unauthenticated_page_for_unlogged_user

import random

def home(request): #nie som prihlaseny
  
  if request.user.is_authenticated:
    logge_user = request.user
    user= User.objects.get(username=logge_user)
    admin_logged = user.is_superuser
    return render(request, 'index.html', {'superuser':admin_logged,})

  else:
    return render(request, 'index.html' )
  

  

  

'''
@login_required(login_url='home')
def logged_home(request): #uz som prihlaseny 
  
  return render(request, 'accounts/logged-page.html')
'''

#REGISTE AND LOGIN AND LOGOUT SECTION

def registerPage(request):
  form = CreateUserForm()

  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      user_name = form.cleaned_data.get('username')
      messages.success(request, "Account was created for "+ user_name)

      return redirect('account:login')

  context = {
    'form':form
  }
  return render(request, 'accounts/register.html', context)


@unauthenticated_page_for_logged_user
def loginPage(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
   
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None: #teda ak user existuje
      login(request, user)
      return redirect('homePage:home')
    else:
      messages.info(request, 'Username OR password is incorrect.')
      

      
  context = {}

  return render(request, 'accounts/login.html', context)


def logoutUser(request):
  logout(request)
  return redirect('homePage:home')



#OTHER VIEW PAGES

def products(request):

  p = Blog.objects.all()

  
  

  context={
    "product": p,
  }
  
  return render(request, 'products.html', context)


@unauthenticated_page_for_unlogged_user
def productPage(request, product_id, product_title_url):
  p = Blog.objects.get(id=product_id)
  
  
  #kazdy refresh stranky sa stane toto 
  products = Blog.objects.all()
  random_three_products = random.choices(products, k=3)
 
  user = request.user
  current_time = timezone.now()
  #print(user)

  context={
   "product": p,
   "sliderProducts": random_three_products,
  }

  
  if request.method == 'POST' and not FavoriteProduct.objects.filter(who_liked=user).exists(): #Toto vytvori usera a prida mu aj konkretny produkt do favorites
    
    FavoriteProduct.objects.create(who_liked=user, added_date=current_time).save()
    favorite = get_object_or_404(FavoriteProduct, who_liked=user)
    favorite.favorite_product.add(p)
    print(favorite)
    
  elif request.method == 'POST' and FavoriteProduct.objects.filter(who_liked=user).exists(): #ak uz user je vytvoreny toto mu prida konkretny produkt do favorites
    favorite = get_object_or_404(FavoriteProduct, who_liked=user)
    print( favorite)
    favorite.favorite_product.add(p)

    return render(request, "product-page.html", context) 
    
  return render(request, "product-page.html", context)


@unauthenticated_page_for_unlogged_user
def FavoriteProductsPage(request):
  
  user = request.user  #zoberie pouzivatela ktory je teraz prihlaseny
  #print(FavoriteProduct.objects.get(who_liked=user))

  logged_user = FavoriteProduct.objects.filter(who_liked=user).first()

  object_not_exist = not FavoriteProduct.objects.filter(who_liked=user).exists()
  
  if request.method == 'GET':

    if not FavoriteProduct.objects.filter(who_liked=user).exists():
      return render(request, 'fav-obj-not-found.html')
     # return  HttpResponse("<h1>"+"ERROR, any object here!"+"</h1>")
    else:
      favorites = logged_user.favorite_product.all()
      latest_favorites = logged_user.favorite_product.all()[0:3]  #  logged_user.favorite_product.order_by('added_date')[:3]
      print(latest_favorites)
  
  
  context={
    'latest_favorites':latest_favorites,
    'favorites': favorites,
  }
  
  return render(request, 'liked-products-page.html', context)



def contact_Page(request):
  #nefunguje

  return render(request, 'contact.html')


def admin_properties(request):
  
  if request.method == 'POST': 
    form = BlogForm(request.POST, request.FILES) 
  
    if form.is_valid(): 
      form.save() 
      return HttpResponse("<h1>"+'successfully uploaded'+'</h1>') 
  else: 
    form = BlogForm() 
    return render(request, 'admin-page.html', {'form' : form}) 
    
  
  
  



  