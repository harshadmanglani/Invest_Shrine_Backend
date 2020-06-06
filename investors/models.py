from django.db import models
from entrepreneurs.models import Industry 

class Portfolio(models.Model): #was InvestorPortfolioModel
    first_name =  models.CharField(max_length = 100, blank = True, null = True) 
    last_name =  models.CharField(max_length = 100, blank = True, null = True)
    email_id = models.EmailField(blank = True, null = True)
    background = models.TextField(blank = True, null = True)
    linkedin_profile = models.URLField(blank = True, null = True)
    interests = models.ManyToManyField('entrepreneurs.Industry', blank = True, null = True) #investor's interests
    investment = models.IntegerField(blank = True, null = True)
    investment_history = models.ManyToManyField('History', blank = True, null = True)
    investment_options = models.ManyToManyField('InvestmentOptions', blank = True, null = True)
    userid = models.IntegerField()

    def __str__(self):
        return str(self.userid)
    
class History(models.Model): #was InvestmentHistoryModel
    investment_history = models.CharField(max_length = 100) 

    def __str__(self): 
        return str(self.investment_history) if self.investment_history else ''

class InvestmentOptions(models.Model): # was InvestmentOptionsModel
    investment_options = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.investment_options) if self.investment_options else ''

   