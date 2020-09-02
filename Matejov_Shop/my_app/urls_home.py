from django.urls import path

from . import views

app_name='homePage'

urlpatterns = [
  path('', views.home, name='home'),
  #path('user-logged', views.logged_home,name='logged-home'),
]