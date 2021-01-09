from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

# Register your models here.
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Carousel)
admin.site.register(Info)
admin.site.register(TypeNews)
admin.site.register(News)
admin.site.register(Vidios,MyModelAdmin)
admin.site.register(Sponsor)
admin.site.register(Address)
admin.site.register(Faculty)
admin.site.register(Major)
admin.site.register(Sosmed)
admin.site.register(Alumni)
