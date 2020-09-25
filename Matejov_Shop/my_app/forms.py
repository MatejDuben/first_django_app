from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .import models


class CreateUserForm(UserCreationForm):

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class ProductForm(forms.ModelForm):
  class Meta:
    model = models.Product
    fields = ['product_title', 'product_description', 'product_image']