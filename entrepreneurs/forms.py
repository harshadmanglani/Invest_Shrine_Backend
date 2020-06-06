from django.forms import ModelForm
from .models import *
from django.utils.translation import gettext_lazy as _

class EntrepreneurPortfolioForm(ModelForm):
    class Meta: 
        model = PortfolioEnt
        fields = '__all__'
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email_id': _('Email ID'),
            'industry': _('Industry'),
            'startup_summary': _('Summarise your business/idea'),
            'investment': _('Initial Investment required'),
            'exec_summary': _('Executive Summary'),
        }

        help_texts = {
            'exec_summary': _('Please describe your summary in related field of work. Be specific about past experience and knowledge in the relevant industry of your startup. This will help investors understand your expertise.'),
            }
    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        hide_condition = kwargs.pop('hide_condition',None)
        super(EntrepreneurPortfolio, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields['userid'].widget = HiddenInput()
        
