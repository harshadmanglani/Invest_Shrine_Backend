from django.forms import ModelForm
from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

class InvestorPortfolioForm(ModelForm): 
    class Meta:
        model = Portfolio # input model to the ModelForm
        fields = '__all__'
        exclude = ('user',)
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'linkedin_profile': _('LinkedIn Profile'),
            'interests': _('Industries of interest'),
            'investment': _('How much money do you plan to invest?'),
            'background': _('Background'),
            'investment_history': _('Investment History'),
            'investment_options': _('Investment Preferences')
        }

        help_texts = {
            'background': _('Please describe your work summary in general, and any specifics you wish to. This will help relevant entrepreneurships reach out to you easily.'),
            'investment_options': _('Please describe your preferred type of funding.')
            }
        
