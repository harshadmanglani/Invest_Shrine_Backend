from django.db import models
from investors.models import * 

# Create your models here.
class Industry(models.Model): # was IndustryModel
    industry = models.CharField(max_length=100) 

    def __str__(self):
        return str(self.industry) if self.industry else ''

class PortfolioEnt(models.Model): #EntrepreneurPortfolioModel
    first_name =  models.CharField(max_length=100, blank = True, null = True)
    last_name =  models.CharField(max_length=100, blank = True, null = True)
    email_id = models.EmailField(blank = True, null = True)
    exec_summary = models.TextField(blank = True, null = True)
    linkedin_profile = models.URLField(blank = True, null = True)
    industry = models.ManyToManyField('Industry', blank = True, null = True)
    startup_summary = models.TextField(blank = True, null = True)
    investment = models.IntegerField(blank = True, null = True)
    investment_options = models.ManyToManyField('investors.InvestmentOptions', blank = True, null = True)
    userid = models.IntegerField()

    def __str__(self):
        return str(self.userid) 

