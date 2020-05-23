from django.forms import ModelForm
from .models import Entrepreneur
from django.utils.translation import gettext_lazy as _

class EntrepreneurForm(ModelForm):
    class Meta:
        model = Entrepreneur
        fields = '__all__'