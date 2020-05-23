from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register(request):

    form = UserCreationForm
    context = {"form" : form}
    
    return render(request = request, template_name = "investors/register_investor.html",
                    context = context)


