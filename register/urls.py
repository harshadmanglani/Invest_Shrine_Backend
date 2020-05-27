
from django.urls import path,include
from . import views
urlpatterns = [
    #path('', views.register, name = "register_investor.html"),
    path('logout/', views.logout_request, name = "login.html"),

]
