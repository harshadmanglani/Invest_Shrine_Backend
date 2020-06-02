from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from .forms import *

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

def portfolio(request):
    form = InvestorPortfolioForm
    if request.method == 'POST': 
        print(request.POST) 
        form = InvestorPortfolioForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, 'entrepreneurs/successful.html')
        else:
            return render(request, 'entrepreneurs/error.html')
    context = {'form': form} 
    return render(request, 'investors/portfolio.html', context)
    



