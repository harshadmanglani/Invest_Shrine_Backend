from django.db import models
from investors.models import * 
from register.models import User as User
 
class Industry(models.Model): # was IndustryModel
    industry = models.CharField(max_length=100) 

    def __str__(self):
        return str(self.industry) if self.industry else ''

    class Meta:
        verbose_name_plural = "Industry"


class Venture(models.Model):
    venture_id = models.AutoField(primary_key= True)
    venture_name = models.CharField(max_length = 300,blank = True, null = True)
    startup_summary = models.TextField(blank = True, null = True)
    industry = models.ManyToManyField('Industry', blank = True)
    website = models.URLField(blank = True, null = True)
    investment = models.IntegerField(blank = True, null = True)
    v_linkedin_profile = models.URLField(blank=True, null = True)
    tag_line = models.CharField(max_length=144, default= None, null = True, blank= True)
    location = models.CharField(max_length=100, default= None, null = True, blank= True)
    logo_image = models.URLField(blank = True, null = True, default= None)
    main_image = models.URLField(blank = True, null = True, default= None)

    def __str__(self):
        return str(self.venture_name)
    
    class Meta:
        verbose_name_plural = "Ventures"



class PortfolioEnt(models.Model): #EntrepreneurPortfolioModel 
    portfolio_id = models.AutoField(primary_key= True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True,related_name = 'entrepreneur_portfolio')
    first_name =  models.CharField(max_length=100, blank = True, null = True)
    last_name =  models.CharField(max_length=100, blank = True, null = True)
    linkedin_profile = models.URLField(blank = True, null = True)
    exec_summary = models.TextField(blank = True, null = True)
    venture = models.ForeignKey(Venture,on_delete = models.CASCADE, null = True)
    display_image = models.URLField(blank = True, null = True, default= None)
    location = models.CharField(max_length=200,blank = True, null = True)
    
    def __str__(self):
        return str(self.first_name)
    
    class Meta:
        verbose_name_plural = "Entrepreneur Portfolio"



