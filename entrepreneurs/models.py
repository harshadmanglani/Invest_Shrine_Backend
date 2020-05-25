from django.db import models
from django import forms

# Create your models here.
class Entrepreneur(models.Model):
    first_name = models.CharField(max_length = 200)
    email_id = models.EmailField()
    password = models.CharField(max_length = 20)

class EntrepreneurPortfolio(models.Model):
    work_exp = models.CharField(max_length = 2000)
    investment_plan = models.ForeignKey('InvestmentPlan', on_delete = models.CASCADE)

class InvestmentPlan(models.Model):
    investment_range = models.CharField(max_length = 20)