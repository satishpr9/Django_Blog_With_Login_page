from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index', views.index, name="index"),
    path('',views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('register',views.register, name="register"),
    
   
    
   
    
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
