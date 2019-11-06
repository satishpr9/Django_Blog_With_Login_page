from django.contrib import admin
from .models import *
from django.contrib.admin.options import ModelAdmin
# Register your models here.

class PostAdmin(ModelAdmin):
    search_fields=['username','Id','email','title']
    list_filter=['date']
admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(Id)