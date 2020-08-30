from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


from .models import Product
from .forms import CreateUserForm

def home(request):
  return render(request, 'index.html')



def products(request):

  p = Product.objects.all()


  context={
    "product": p,
  }

  return render(request, 'products.html', context)


def register(request):
  form = CreateUserForm()

  if request.method == "POST":
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
  '''
  {% csrf_token %}
  {{form.as_p}}
  '''

  context = {
    'form':form
  }
  return render(request, 'accounts/register.html', context)

def login(request):
  return render(request, 'accounts/login.html')