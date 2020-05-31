from django.db import models
from django import forms

# Create your models here.
class EntrepreneurModel(models.Model):
    first_name = models.CharField(max_length = 200)
    email_id = models.EmailField()
    #industry = models.ForeignKey('IndustryModel', on_delete = models.CASCADE)
    work_exp = models.TextField()
    #investment_plan = models.ForeignKey('InvestmentPlanModel', on_delete = models.CASCADE)