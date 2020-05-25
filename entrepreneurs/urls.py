from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.register, name = "entrepreneur_registration"),
    path('portfolio/', views.portfolio, name = "entrepreneur_portfolio"),
]
