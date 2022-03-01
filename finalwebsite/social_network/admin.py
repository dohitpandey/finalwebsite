from django.contrib import admin
from .models import user

class USER(admin.ModelAdmin):
    list_display = ('name','phone','email','password','profile_pic')
admin.site.register(user,USER)