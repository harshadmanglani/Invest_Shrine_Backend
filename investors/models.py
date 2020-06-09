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
    #email_id = models.EmailField(blank = True, null = True)
    background = models.TextField(blank = True, null = True)
    linkedin_profile = models.URLField(blank = True, null = True)
    interests = models.ManyToManyField('entrepreneurs.Industry') #investor's interests
    investment = models.IntegerField(blank = True, null = True)
    investment_history = models.ManyToManyField('History')
    investment_options = models.ManyToManyField('InvestmentOptions')
    

    def __str__(self):
        return self.email_id 
    
class History(models.Model): #was InvestmentHistoryModel
    investment_history = models.CharField(max_length = 100) 

    def __str__(self):
        return self.investment_history

class InvestmentOptions(models.Model): # was InvestmentOptionsModel
    investment_options = models.CharField(max_length = 100)

    def __str__(self):
        return self.investment_options



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('****', created)
    if instance.is_investor:
        Portfolio.objects.get_or_create(user = instance)
    else:
        EntrepreneurPortfolio.objects.get_or_create(user = instance)
	
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print('_-----')	
    # print(instance.internprofile.bio, instance.internprofile.location)
    if instance.is_investor:
        instance.investor_portfolio.save()
    else:
        EntrepreneurPortfolio.objects.get_or_create(user = instance)
   