from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField


class Blog(models.Model):
  product_title = models.CharField(max_length=200, verbose_name='nadpis Blogu')
  product_description = models.TextField(verbose_name='Text', blank=False)
  product_image = models.ImageField(upload_to='uploaded_posts', blank=False, null=True, verbose_name='obrazok')


  blog_description2 = models.TextField(verbose_name='Text2' , blank=True)
  blog_figure2 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='obrazok pod text2')
  blog_figure2_des = TextField(max_length=300, verbose_name="popis obrazku2", blank=True)
  blog_figure2_2 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='druhy obrazok pod text2')
  blog_figure2_2_des = TextField(max_length=300, verbose_name="popis obrazku2_2", blank=True)

  blog_description3 = models.TextField(verbose_name='Text3', blank=True)
  blog_figure3 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='obrazok pod text3')
  blog_figure3_des = TextField(max_length=300, verbose_name="popis obrazku3", blank=True)
  blog_figure3_2 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='druhy obrazok pod text3')
  blog_figure3_2_des = TextField(max_length=300, verbose_name="popis obrazku3_2", blank=True)

  blog_description4 = models.TextField(verbose_name='Text4', blank=True)
  blog_figure4 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='obrazok pod text4')
  blog_figure4_des = TextField(max_length=300, verbose_name="popis obrazku4", blank=True)
  blog_figure4_2 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='druhy obrazok pod text4')
  blog_figure4_2_des = TextField(max_length=300, verbose_name="popis obrazku4_2", blank=True)

  blog_description5 = models.TextField(verbose_name='Text5', blank=True)
  blog_figure5 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='obrazok pod text5')
  blog_figure5_des = TextField(max_length=300, verbose_name="popis obrazku5", blank=True)
  blog_figure5_2 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='druhy obrazok pod text5')
  blog_figure5_2_des = TextField(max_length=300, verbose_name="popis obrazku5_2", blank=True)

  blog_description6 = models.TextField(verbose_name='Text6', blank=True)
  blog_figure6 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='obrazok pod text6')
  blog_figure6_des = TextField(max_length=300, verbose_name="popis obrazku6", blank=True)
  blog_figure6_2 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='druhy obrazok pod text6')
  blog_figure6_2_des = TextField(max_length=300, verbose_name="popis obrazku6_2", blank=True)

  blog_description7 = models.TextField(verbose_name='Text7', blank=True)
  blog_figure7 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='obrazok pod text7')
  blog_figure7_des = TextField(max_length=300, verbose_name="popis obrazku7", blank=True)
  blog_figure7_2 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='druhy obrazok pod text7')
  blog_figure7_2_des = TextField(max_length=300, verbose_name="popis obrazku7_2", blank=True)

  blog_description8 = models.TextField(verbose_name='Text8', blank=True)
  blog_figure8 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='obrazok pod text8')
  blog_figure8_des = TextField(max_length=300, verbose_name="popis obrazku8", blank=True)
  blog_figure8_2 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='druhy obrazok pod text8')
  blog_figure8_2_des = TextField(max_length=300, verbose_name="popis obrazku8_2", blank=True)

  blog_description9 = models.TextField(verbose_name='Text9', blank=True)
  blog_figure9 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='obrazok pod text9')
  blog_figure9_des = TextField(max_length=300, verbose_name="popis obrazku9", blank=True)
  blog_figure9_2 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='druhy obrazok pod text9')
  blog_figure9_2_des = TextField(max_length=300, verbose_name="popis obrazku9_2", blank=True)

  blog_description10 = models.TextField(verbose_name='Text10', blank=True)
  blog_figure10 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='obrazok pod text10')
  blog_figure10_des = TextField(max_length=300, verbose_name="popis obrazku10", blank=True)
  blog_figure10_2 = models.ImageField(upload_to='uploaded_posts', blank=True, null=True, verbose_name='druhy obrazok pod text10')
  blog_figure10_2_des = TextField(max_length=300, verbose_name="popis obrazku10_2", blank=True)
  
  



  def __str__(self):
    return self.product_title
  

class FavoriteBlog(models.Model):
  who_liked = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="použivatel ktorému sa to páči")
  favorite_product = models.ManyToManyField(Blog, related_name="favorite_post", verbose_name="blog ktorý sa mu páči")
  added_date = models.DateTimeField('date_added',)

  def __str__(self):
    return str(self.who_liked)