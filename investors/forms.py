from django.forms import ModelForm
from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

# handle one - portfolio form for investors - define labels and help texts better - HIDE user ID
class InvestorPortfolioForm(ModelForm): 
    class Meta:
        model = Portfolio # input model to the ModelForm
        fields = '__all__'
        # exclude = ('user',)
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email_id': _('Email ID'),
            'interests': _('Industry'),
            'investment': _('Initial Investment required'),
            'background': _('Background'),
        }

        help_texts = {
            'background': _('Please describe your work summary in general, and any specifics you wish to. This will help relevant entrepreneurships reach out to you easily.'),
            }
        
