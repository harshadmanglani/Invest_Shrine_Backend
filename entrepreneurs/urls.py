from django.urls import path,include
from . import views
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    path('portfolio/', views.portfolio, name = "entrepreneur_portfolio"),
    
    path('homepage/', views.entrepreneur_homepage, name = 'entrepreneur_homepage'),
    path('homepage/<int:pk>/', views.investor_slug, name = 'investor_slug'),
    
]
