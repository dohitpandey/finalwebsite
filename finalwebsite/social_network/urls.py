from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.login,name='login' ),
    path('signup/',views.signup,name='signup' ),
    path('homepage/',views.save,name='save'),
    path('homepage/',views.save,name='check'),
]