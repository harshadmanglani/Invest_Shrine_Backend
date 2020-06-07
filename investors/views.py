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
   return user_passes_test(in_groups)
"""



@login_required(login_url='/login/')
#@group_required('Investors')
def investor_homepage(request):
    """
    Renders the investor homepage with mini portfolios of entrepreneurs, filter functionality not available
    yet. Sending all entrepreneur portfolios from the database as of now.
    """
    allEntrepreneurs = Entrepreneur.objects.all()
    context = {"Entrepreneurs" : allEntrepreneurs}
    return render(request= request, template_name = "investors/homepage.html", context = context)

def entrepreneur_slug(request,pk):
    """
    Renders the page for an invidividual entrepreneur portfolio, maybe we could figure out a better way instead of
    explicitly sending industry_list and options, they're already a part of variable ent.
    """
    ent = Entrepreneur.objects.get(pk=pk)
    industry_list = ent.industry.all() # sending this separately - can be replaced if {{industry.all}} can be iterated in templates.html
    options = ent.investment_options.all() # sending this separately - can be replaced
    context = {"details" : ent, "industry_list": industry_list, "options": options}
    return render(request = request, template_name = "investors/ent_slug.html",context = context)


def portfolio(request): 
    """
    Renders a pre-populated portfolio connected to the user registration table. Functionality for prepopulation is broken 
    as of now.
    """
    if 'investor_uid' in request.session:
        investor_uid = int(request.session.get('investor_uid','-1'))
        if investor_uid == -1:
            print("something went wrong")
            return render(request, 'entrepreneurs/error.html')
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
            return redirect('/investors/homepage/') # changed this from render /successful.html
        else:
            return render(request, 'entrepreneurs/error.html') # let this remain

    context = {'form': form} 
    return render(request, '/investors/portfolio.html', context)
    



