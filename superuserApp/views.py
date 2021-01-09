from django.shortcuts import render,HttpResponse,redirect
from django.conf import settings
from .models import *

# Create your views here.

def index(request):
   title = "Beranda"
   carousel = Carousel.objects.all()
   info = Info.objects.get(id=1)
   news = News.objects.all()
   video = Vidios.objects.all()
   sponsor = Sponsor.objects.all()

   conteks = {
      'title':title,
      'carousel':carousel,
      'info':info,
      'news':news,
      'videos':video,
      'sponsor':sponsor,
   }
   return render(request,'index.html',conteks)

def about(request):
   title = "Tentang ITB"
   conteks = {
      'title':title,
   }
   return render(request,'about.html',conteks)

def faculty(request):
   title = "Fakultas dan Sekolah"
   conteks = {
      'title':title,
   }
   return render(request,'faculty.html',conteks)

def detail_info(request):
   pass

