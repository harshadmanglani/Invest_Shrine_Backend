
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('login/', views.login_request, name = 'login'),
    path('logout/', views.logout_request, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact_us, name = 'contact'),
    path('portfolio/', views.portfolio, name = 'portfolio')
]
