from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required = True)
    category = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username','email','password1','password2','category')

    def save(self, commit = True):
        user = super(NewUserForm,self).save(commit=False)
        user.email= self.cleaned_data("email")
        user.category = self.cleaned_data("category")
        if commit:
            user.save()
            return user