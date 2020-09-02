from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .models import Product
from .forms import CreateUserForm
from .decorators import unauthenticated_user

def home(request): #nie som prihlaseny
  
  return render(request, 'index.html')

'''
@login_required(login_url='home')
def logged_home(request): #uz som prihlaseny 
  
  return render(request, 'accounts/logged-page.html')
'''

def products(request):

  p = Product.objects.all()


  context={
    "product": p,
  }
  
  return render(request, 'products.html', context)

def productPage(request, product_id, product_title_url):
  p = Product.objects.get(id=product_id)
  context={
    "product": p,
  }

  return render(request, "product-page.html", context)



def LikedProductsPage(request):




  return render(request, "liked-products-page.html")


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


@unauthenticated_user
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