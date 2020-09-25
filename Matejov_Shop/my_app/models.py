from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
  product_title = models.CharField(max_length=200)
  product_description = models.CharField(max_length=1000)
  product_image = models.ImageField(upload_to='uploaded_posts', blank=True, null=True)

  def __str__(self):
    return self.product_title
  

class FavoriteProduct(models.Model):
  who_liked = models.ForeignKey(User, on_delete=models.CASCADE)
  favorite_product = models.ManyToManyField(Product, related_name="favorite_post")
  added_date = models.DateTimeField('date_added')

  def __str__(self):
    return str(self.who_liked)