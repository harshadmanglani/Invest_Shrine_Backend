from django.db import models
from investors.models import * 
from register.models import User as User
 
class Industry(models.Model): # was IndustryModel
    industry = models.CharField(max_length=100) 

    def __str__(self):
        return str(self.industry) if self.industry else ''

class Venture(models.Model):
    venture_name = models.CharField(max_length = 300,blank = True, null = True)
    startup_summary = models.TextField(blank = True, null = True)
    industry = models.ManyToManyField('Industry', blank = True)
    website = models.URLField(blank = True, null = True)
    investment = models.IntegerField(blank = True, null = True)
    investment_options = models.ManyToManyField('investors.InvestmentOptions', blank = True)

    def __str__(self):
        return str(self.venture_name)


class PortfolioEnt(models.Model): #EntrepreneurPortfolioModel 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True,related_name = 'entrepreneur_portfolio')
    first_name =  models.CharField(max_length=100, blank = True, null = True)
    last_name =  models.CharField(max_length=100, blank = True, null = True)
    linkedin_profile = models.URLField(blank = True, null = True)
    exec_summary = models.TextField(blank = True, null = True)
    venture = models.ForeignKey(Venture,on_delete = models.CASCADE, null = True)

    def __str__(self):
        return str(self.first_name)


