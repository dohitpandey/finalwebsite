from django.contrib import admin
from .models import user,friends

class USER(admin.ModelAdmin):
    list_display = ('name','phone','email','password','profile_pic','id','nameslug')
admin.site.register(user,USER)

class FRIENDS(admin.ModelAdmin):
    list_display = ('id','lou',)
admin.site.register(friends,FRIENDS)