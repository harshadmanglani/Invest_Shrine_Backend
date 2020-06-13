from django.shortcuts import render, redirect
from .models import Portfolio as InvestorPortfolio
from .forms import InvestorPortfolioForm as InvestorPortfolioForm
from entrepreneurs.models import PortfolioEnt as Entrepreneur
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import user_passes_test 


def investor_check(user):
    """
    This is a decorator which checks if the user is registered as an investor and returns a boolean
    variable which is used to redirect(Configure URL redirects after testing this functionality). 
    """
    if not user.is_superuser:
        investors = InvestorPortfolio.objects.all()
        print(investors)
        return investors.filter(user=user).exists()
    else:
        return user.is_superuser


@login_required
@user_passes_test(investor_check, login_url = '/')
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
@user_passes_test(investor_check, login_url = '/')
def investor_homepage(request):
    """
    Renders the investor homepage with mini portfolios of entrepreneurs, filter functionality not available
    yet. Sending all entrepreneur portfolios from the database as of now.
    """

    allEntrepreneurs = Entrepreneur.objects.all()
    context = {"Entrepreneurs" : allEntrepreneurs}
    return render(request= request, template_name = "investors/homepage.html", context = context)


@login_required
@user_passes_test(investor_check, login_url = '/')
def entrepreneur_slug(request,pk):
    """
    Renders the page for an invidividual entrepreneur portfolio, optimised to retrieve all data from the entrepreneur
    variable.
    """

    entrepreneur = Entrepreneur.objects.get(pk=pk)
    context = {"entrepreneur" : entrepreneur}
    return render(request = request, template_name = "investors/ent_slug.html",context = context)



