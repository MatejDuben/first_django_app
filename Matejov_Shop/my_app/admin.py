from django.contrib import admin
from .models import Product, FavoriteProduct

admin.site.register(Product)
admin.site.register(FavoriteProduct)