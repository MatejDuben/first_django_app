from django.db import models


class Product(models.Model):
  product_title = models.CharField(max_length=200)
  product_description = models.CharField(max_length=1000)
  product_image = models.FileField(upload_to='uploaded_posts', blank=True)

  def __str__(self):
    return self.product_title