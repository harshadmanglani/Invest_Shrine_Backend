from django.db import models
from investors.models import *

# Create your models here.
class Industry(models.Model): # was IndustryModel
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.industry

class PortfolioEnt(models.Model): #EntrepreneurPortfolioModel
    first_name =  models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    email_id = models.EmailField()
    exec_summary = models.TextField()
    linkedin_profile = models.URLField()
    industry = models.ManyToManyField('Industry')
    startup_summary = models.TextField()
    investment = models.IntegerField()
    investment_options = models.ManyToManyField('investors.InvestmentOptions')

    def __str__(self):
        return self.email_id

