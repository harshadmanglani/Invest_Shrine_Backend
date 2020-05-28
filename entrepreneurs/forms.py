from django.forms import ModelForm
from .models import *
from django.utils.translation import gettext_lazy as _

class EntrepreneurForm(ModelForm):
    class Meta:
        model = EntrepreneurModel
        fields = '__all__'

class EntrepreneurPortfolioForm(ModelForm):
    class Meta:
        model = EntrepreneurPortfolioModel
        fields = '__all__'