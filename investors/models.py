from django.db import models
from entrepreneurs.models import Industry

class Portfolio(models.Model): #was InvestorPortfolioModel
    first_name =  models.CharField(max_length = 100)
    last_name =  models.CharField(max_length = 100)
    email_id = models.EmailField()
    background = models.TextField()
    linkedin_profile = models.URLField()
    interests = models.ManyToManyField('entrepreneurs.Industry') #investor's interests
    investment = models.IntegerField()
    investment_history = models.ManyToManyField('History')
    investment_options = models.ManyToManyField('InvestmentOptions')

    def __str__(self):
        return self.email_id
    
class History(models.Model): #was InvestmentHistoryModel
    investment_history = models.CharField(max_length = 100) 

    def __str__(self):
        return self.investment_history

class InvestmentOptions(models.Model): # was InvestmentOptionsModel
    investment_option = models.CharField(max_length = 100)

    def __str__(self):
        return self.investment_options

   