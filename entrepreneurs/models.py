from django.db import models
from django import forms

# Create your models here.
class IndustryModel(models.Model):
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.industry

class EntrepreneurPortfolioModel(models.Model):
    first_name =  models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    email_id = models.EmailField()
<<<<<<< HEAD
    #industry = models.ForeignKey('IndustryModel', on_delete = models.CASCADE)
    work_exp = models.TextField()
    #investment_plan = models.ForeignKey('InvestmentPlanModel', on_delete = models.CASCADE)
=======
    industry = models.ManyToManyField('IndustryModel')
    startup_summary = models.TextField()
    investment = models.IntegerField()
    exec_summary = models.TextField()

    def __str__(self):
        return self.email_id

>>>>>>> 2b2c3f1d0333b78083d76031d303f72098c66fcd
