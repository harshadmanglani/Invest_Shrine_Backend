from django.db import models

class Investor(models.Model):
    investor_name = models.CharField(max_length=200)
    investor_email = models.EmailField()
    investor_desc = models.CharField(max_length = 300)
    investor_money = models.CharField(max_length =20)

    #This is a trial model to create a prototype homepage
    #here i am not including an investor slug because storing slugs for each investor is too much 
    # we will just open Urls according to their investor id 
    
    