from django.shortcuts import render,HttpResponse,redirect
from django.conf import settings
from .models import *

# Create your views here.

def index(request):
   carousel = Carousel.objects.all()
   info = Info.objects.get(id=1)
   news = News.objects.all()
   video = Vidios.objects.all()
   sponsor = Sponsor.objects.all()

   conteks = {
      'carousel':carousel,
      'info':info,
      'news':news,
      'videos':video,
      'sponsor':sponsor,
   }
   return render(request,'index.html',conteks)

def detail_info(request):
   pass

