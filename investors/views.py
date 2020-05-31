from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Investor

"""def register(request):

    form = UserCreationForm
    context = {"form" : form}
    
    return render(request = request, template_name = "investors/register_investor.html",
                    context = context)"""


def investor_homepage(request):
    allInvestors = Investor.objects.all()
    context = {"investors" : allInvestors}

    return render(request= request, template_name = "investors/homepage.html", context = context)

#def investor_slug(request,pk)

def about(request):
   # context = {"about" : "hey this is Aditya"}

    return render(request=request, template_name = "investors/about.html") #,context = context)

def contact_us(request):
    return render(request = request,template_name = "investors/contact.html")
    



