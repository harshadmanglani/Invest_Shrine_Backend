
from django.urls import path,include
from . import views
urlpatterns = [
    #path('register/', views.register, name = "register_investor.html"),
    path('homepage/', views.investor_homepage, name = "investor_homepage"),


]
