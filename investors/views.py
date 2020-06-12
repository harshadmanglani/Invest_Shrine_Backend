from django.shortcuts import render, redirect
from .models import Portfolio as InvestorPortfolio
from .forms import InvestorPortfolioForm as InvestorPortfolioForm
from entrepreneurs.models import PortfolioEnt as Entrepreneur
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import user_passes_test 

@login_required
def portfolio(request): 
    """
    Renders a prepopulated, ready to edit & update portfolio
    """
    
    obj = InvestorPortfolio.objects.get(user = request.user)
    form = InvestorPortfolioForm(initial=model_to_dict(obj))
    if request.method == 'POST': 
        form = InvestorPortfolioForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('/investors/homepage/') # changed this from render /successful.html
        else:
            print(form.errors)
            return render(request, 'entrepreneurs/error.html') # let this remain

    context = {'form': form} 
    return render(request, 'investors/portfolio.html', context)

@login_required
def investor_homepage(request):
    """
    Renders the investor homepage with mini portfolios of entrepreneurs, filter functionality not available
    yet. Sending all entrepreneur portfolios from the database as of now.
    """

    allEntrepreneurs = Entrepreneur.objects.all()
    context = {"Entrepreneurs" : allEntrepreneurs}
    return render(request= request, template_name = "investors/homepage.html", context = context)

@login_required
def entrepreneur_slug(request,pk):
    """
    Renders the page for an invidividual entrepreneur portfolio, maybe we could figure out a better way instead of
    explicitly sending industry_list and options, they're already a part of variable entrepreneur.
    """

    entrepreneur = Entrepreneur.objects.get(pk=pk)
    industry_list = entrepreneur.industry.all() # sending this separately - can be replaced if {{industry.all}} can be iterated in templates.html
    options = ent.investment_options.all() # sending this separately - can be replaced
    context = {"details" : entrepreneur, "industry_list": industry_list, "options": options}
    return render(request = request, template_name = "investors/ent_slug.html",context = context)



