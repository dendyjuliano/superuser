from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Carousel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img_carousel',null=True)

    def __str__(self):
        return self.name

class Info(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img_info',null=True)
    description = models.TextField(max_length=999)
    city = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TypeNews(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=100)
    type = models.ForeignKey(TypeNews,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='img_news',null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=999)

    def __str__(self):
        return self.title
    
class Vidios(models.Model):
    video = EmbedVideoField()

    def __str__(self):
        return self.video

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img_sponsor')

    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    email = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img_address') 

    def __str__(self):
        return self.name