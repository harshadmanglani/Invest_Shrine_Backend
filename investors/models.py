from django.db import models
from entrepreneurs.models import Industry
from entrepreneurs.models import PortfolioEnt as EntrepreneurPortfolio
from register.models import User as User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Portfolio(models.Model): #was InvestorPortfolioModel
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True,related_name = "investor_portfolio")
    first_name =  models.CharField(max_length = 100, blank = True, null = True) 
    last_name =  models.CharField(max_length = 100, blank = True, null = True)
    current_occupation = models.CharField(max_length=100, blank = True, null = True)
    linkedin_profile = models.URLField(blank = True, null = True)
    background = models.TextField(blank = True, null = True)
    interests = models.ManyToManyField('entrepreneurs.Industry') #investor's interests
    investment = models.IntegerField(blank = True, null = True)
    investment_history = models.ManyToManyField('History')
    investment_options = models.ManyToManyField('InvestmentOptions', blank = True)

    def __str__(self):
        return str(self.first_name)                                           # don't modify
    
# investment history - public markets, direct investment, etc as a seasoned investor
class History(models.Model): #was InvestmentHistoryModel
    investment_history = models.CharField(max_length = 100) 

    def __str__(self): 
        return str(self.investment_history) if self.investment_history else '' # don't modify

# preferred investment options - funding for equity, funding for x% interest, etc
class InvestmentOptions(models.Model): # was InvestmentOptionsModel
    investment_options = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.investment_options) if self.investment_options else '' # don't modify

#watchlist table for investors
class WatchList(models.Model):
    investor = models.ForeignKey(Portfolio, on_delete= models.CASCADE, null = True, blank =True)
    entrepreneurs = models.ManyToManyField(EntrepreneurPortfolio, blank = True)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.category == 'Investor':
        print('investor portfolio created:', created)
        Portfolio.objects.get_or_create(user = instance)
    elif instance.category == 'Entrepreneur':
        print('entrepreneur portfolio created:', created)
        EntrepreneurPortfolio.objects.get_or_create(user = instance)
    else:
        pass
	
@receiver(post_save, sender=User) 
def save_user_profile(sender, instance, **kwargs):
    if instance.category == 'Investor':
        instance.investor_portfolio.save()
        print('investor portfolio saved')
    elif instance.category == 'Entrepreneur':
        instance.entrepreneur_portfolio.save()
        print('entrepreneur portfolio saved')
    else:
        pass
   
