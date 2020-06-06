from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Portfolio as InvestorPortfolio
from .forms import *
from entrepreneurs.models import PortfolioEnt as Entrepreneur
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
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
    industry_list = ent.industry.all()
    options = ent.investment_options.all()
    context = {"details" : ent, "industry_list": industry_list, "options": options}
    return render(request = request, template_name = "investors/ent_slug.html",context = context)


def portfolio(request): 
    populate = False
    if 'investor_uid' in request.session:
        populate = True
        investor_uid = int(request.session.get('investor_uid','-1'))
        if investor_uid == -1:
            print("something is horribly wrong")
        print(investor_uid)
        print(InvestorPortfolio.objects.filter(userid = investor_uid))
        invobj = InvestorPortfolio.objects.filter(userid = investor_uid)[0]
        print(invobj)
        form = InvestorPortfolioForm(initial = model_to_dict(invobj))

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
    



