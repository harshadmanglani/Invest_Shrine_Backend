
from django.urls import path,include
from . import views
urlpatterns = [
    path('homepage/', views.investor_homepage, name = 'investor_homepage'),
    path('portfolio/', views.portfolio, name = 'investor_portfolio'),
    path('homepage/<int:pk>', views.entrepreneur_slug, name = 'entrepreneur_slug'),
    
]
