from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from .forms import *
from entrepreneurs.models import EntrepreneurPortfolioModel as Entrepreneur
"""def register(request):

    form = UserCreationForm
    context = {"form" : form}
    
    return render(request = request, template_name = "investors/register_investor.html",
                    context = context)"""


def investor_homepage(request):
    allEntrepreneurs = Entrepreneur.objects.all()
    context = {"Entrepreneurs" : allEntrepreneurs}

    return render(request= request, template_name = "investors/homepage.html", context = context)

def entrepreneur_slug(request,pk):
    ent = Entrepreneur.objects.get(pk=pk)
    context = {"details" : ent}
    return render(request = request, template_name = "investors/ent_slug.html",context = context)


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
    



