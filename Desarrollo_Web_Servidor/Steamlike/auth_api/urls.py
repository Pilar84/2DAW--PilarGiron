from django.urls import path
from .views import register, login_view


urlpatterns = [
    path("register/", register),
    path("login/", login_view), 
    path("api/auth/logout/", login_view),
      
    
]

