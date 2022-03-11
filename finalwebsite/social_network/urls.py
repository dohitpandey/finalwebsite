from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('homepage/',views.home,name='homepage'),
    path('home/',views.save,name='save&check'),
    path('friend/',views.friend,name='friend'),
    path('suggestions/',views.suggestions,name='suggestions'),
    path('profile/<slug:slugname>/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)