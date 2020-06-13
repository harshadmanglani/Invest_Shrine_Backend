from django.db import models
from django.contrib.auth.models import AbstractUser
    
class User(AbstractUser):
    email = models.EmailField()
    INVESTOR = 'Investor'
    ENTREPRENEUR = 'Entrepreneur'
    category = models.CharField(
        choices = [(INVESTOR, 'Investor'),
        (ENTREPRENEUR, 'Entrepreneur'),], 
        max_length = 20,
        default = INVESTOR)




