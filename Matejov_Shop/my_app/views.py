from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Product


def home(request):
  return render(request, 'index.html')



def products(request):

  p = Product.objects.all()


  context={
    "product": p,
  }

  return render(request, 'products.html', context)