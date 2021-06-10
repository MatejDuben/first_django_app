from django.urls import path

from . import views

app_name='productPage'
urlpatterns = [
  path('', views.products, name='products'),
  path('<str:product_id>/<str:product_title_url>/', views.productPage, name="thisProduct")
] 