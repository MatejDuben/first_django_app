"""Matejov_Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from my_app import views

urlpatterns = [
    path('', include("my_app.urls_home")),
    path('blogs/', include("my_app.urls_blog")),
    path('account/', include("my_app.urls_account")),
    path('favorite-products/', views.FavoriteProductsPage, name='likedPage'),
    path('contact/', views.contact_Page, name='contactPage'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)