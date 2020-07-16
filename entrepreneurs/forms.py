from django.forms import ModelForm
from .models import *
from django.utils.translation import gettext_lazy as _

class EntrepreneurPortfolioForm(ModelForm):
    class Meta: 
        model = PortfolioEnt 
        fields = '__all__'
        exclude = ('user',)
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email_id': _('Email ID'),
            'industry': _('Industry'),
            'startup_summary': _('Summarise your business/idea'),
            'investment': _('Initial Investment required'),
            'exec_summary': _('Executive Summary'),
            'linkedin_profile': _('LinkedIn Profile'),
            'investment_options': _('Investment Preferences'),
            'venture_name': _('Name of your venture'),
            'prototype': _('Pitch Deck')
        }

        help_texts = {
            'exec_summary': _('Please describe your summary in related field of work. Be specific about past experience and knowledge in the relevant industry of your startup. This will help investors understand your expertise.'),
            'investment_options': _('Please describe your preferred type of funding.'),
            'prototype': _('A secure GDrive link to your pitch deck, please leave it blank in case it is not ready.')
            }
        

#making the forms for graphql api
class EntForm(ModelForm):
    class Meta: 
        model = PortfolioEnt 
        fields = '__all__'

class VentureForm(ModelForm):
    class Meta: 
        model = Venture 
        fields = '__all__'
    
