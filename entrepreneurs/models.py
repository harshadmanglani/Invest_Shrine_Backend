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
    industry = models.ManyToManyField('IndustryModel')
    startup_summary = models.TextField()
    investment = models.IntegerField()
    exec_summary = models.TextField()

    def __str__(self):
        return self.email_id

