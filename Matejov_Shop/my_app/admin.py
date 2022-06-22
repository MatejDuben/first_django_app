from django.contrib import admin
from .models import Blog, FavoriteBlog

admin.site.register(Blog)
admin.site.register(FavoriteBlog)