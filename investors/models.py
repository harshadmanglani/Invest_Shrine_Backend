from django.db import models
from entrepreneurs.models import IndustryModel

class InvestorPortfolioModel(models.Model):
    first_name =  models.CharField(max_length = 100)
    last_name =  models.CharField(max_length = 100)
    email_id = models.EmailField()
    background = models.TextField()
    linkedin_profile = models.URLField()
    interests = models.ManyToManyField('entrepreneurs.IndustryModel') #investor's interests
    investment = models.IntegerField()
    investment_history = models.ManyToManyField('InvestmentHistoryModel')
    investment_options = models.ManyToManyField('InvestmentOptionsModel')

    def __str__(self):
        return self.email_id
    
class InvestmentHistoryModel(models.Model):
    investment_history = models.CharField(max_length = 100) 

    def __str__(self):
        return self.investment_history

class InvestmentOptionsModel(models.Model):
    investment_option = models.CharField(max_length = 100)

    def __str__(self):
        return self.investment_options

   