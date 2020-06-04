
from django.urls import path,include
from . import views
urlpatterns = [
    #path('', views.register, name = "register_investor.html"),
    path('', views.homepage, name = "homepage"),
    path('login', views.login_request, name = "login"),
    path('logout', views.logout_request, name = "logout"),
    path('register', views.register, name = "register"),
   
]
