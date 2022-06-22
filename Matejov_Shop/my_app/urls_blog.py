from django.urls import path

from . import views

app_name='blogPage'
urlpatterns = [
  path('', views.products, name='blog'),
  path('<str:product_id>/<str:product_title_url>/', views.productPage, name="thisBlog")
] 