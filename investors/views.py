from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from .forms import *
from entrepreneurs.models import PortfolioEnt as Entrepreneur
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test


"""
def group_required(*group_names):
  #Requires user membership in at least one of the groups passed in.

   def in_groups(u):
       if u.is_authenticated:
           if bool(u.groups.filter(name__in =group_names)) | u.is_superuser:
               return True
       return False
   return user_passes_test(in_groups)"""



@login_required(login_url='/login/')
#@group_required('Investors')
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
    



