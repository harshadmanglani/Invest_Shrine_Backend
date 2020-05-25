from django.forms import ModelForm
from .models import *
from django.utils.translation import gettext_lazy as _

class EntrepreneurForm(ModelForm):
    class Meta:
        model = Entrepreneur
        fields = '__all__'

class EntrepreneurPortfolioForm(ModelForm):
    class Meta:
        model = EntrepreneurPortfolio
        fields = '__all__'