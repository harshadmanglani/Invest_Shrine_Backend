from django.db import models
from investors.models import * 
from register.models import User as User

# Create your models here.
class Industry(models.Model): # was IndustryModel
    industry = models.CharField(max_length=100) 

    def __str__(self):
        return str(self.industry) if self.industry else ''

class PortfolioEnt(models.Model): #EntrepreneurPortfolioModel
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True,related_name = "entrepreneur_portfolio")
    first_name =  models.CharField(max_length=100, blank = True, null = True)
    last_name =  models.CharField(max_length=100, blank = True, null = True)
    # email_id = models.EmailField(blank = True, null = True)
    exec_summary = models.TextField(blank = True, null = True)
    linkedin_profile = models.URLField(blank = True, null = True)
    industry = models.ManyToManyField('Industry')
    startup_summary = models.TextField(blank = True, null = True)
    investment = models.IntegerField(blank = True, null = True)
    investment_options = models.ManyToManyField('investors.InvestmentOptions')

    def __str__(self):
        return str(self.user)

