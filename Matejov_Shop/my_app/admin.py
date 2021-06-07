from django.contrib import admin
from .models import Blog, FavoriteProduct

admin.site.register(Blog)
admin.site.register(FavoriteProduct)