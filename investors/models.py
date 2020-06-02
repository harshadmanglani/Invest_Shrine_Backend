from django.db import models
from entrepreneurs.models import IndustryModel

class Investor(models.Model):
    investor_name = models.CharField(max_length=200)
    investor_email = models.EmailField()
    investor_desc = models.CharField(max_length = 300)
    investor_money = models.CharField(max_length =20)

    #This is a trial model to create a prototype homepage
    #here i am not including an investor slug because storing slugs for each investor is too much 
    # we will just open Urls according to their investor id 

class InvestorPortfolioModel(models.Model):
    first_name =  models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    email_id = models.EmailField()
    interests = models.ManyToManyField('entrepreneurs.IndustryModel') #investor's interests
    investment = models.IntegerField()
    background = models.TextField()

    def __str__(self):
        return self.email_id
    
    