
from django.urls import path,include
from . import views
urlpatterns = [
    #path('', views.register, name = "register_investor.html"),
    path('', views.homepage, name = "homepage"),
    path('login/', views.login_request, name = "login"),
    path('logout/', views.logout_request, name = "logout"),
    path('register/', views.register, name = "register"),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact_us, name = 'contact'),
    #temp urls for test
    path('investor_register/', views.investor_register, name = 'investor_register'),
    
]
