from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

# the new user form to let people sign up, might need to remove email because it's redundant. better to keep the email
# both places until we link both tables successfully.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required = True)
    #category = forms.ModelChoiceField(queryset=Category.objects, required=True, label=_("Status"))

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    # def save(self, commit = True):
    #     user = super(NewUserForm,self).save(commit=False)
    #     user.email= self.cleaned_data.get("email")
    #     #user.category = self.cleaned_data.get("category")
    #     if commit:
    #         user.save()
    #         return user
