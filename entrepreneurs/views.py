from django.shortcuts import render, redirect
from .forms import EntrepreneurPortfolioForm as EntrepreneurPortfolioForm
from investors.models import Portfolio as Investors
from .models import PortfolioEnt as EntrepreneurPortfolio 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms.models import model_to_dict 


#Make custom decorators here to check user permissions
def entrepreneur_check(user):
    """
    This is a decorator which checks if the user is registered as an entrepreneur and returns a boolean
    variable which is used to redirect(Configure URL redirects after testing this functionality). 
    """
    if not user.is_superuser:
        entrepreneurs = EntrepreneurPortfolio.objects.all()
        print(entrepreneurs)
        return entrepreneurs.filter(user=user).exists()
    else:
        return user.is_superuser


@login_required
@user_passes_test(entrepreneur_check,login_url = '/')
def portfolio(request):
    """
    Renders a prepopulated, ready to edit & update portfolio
    """

    obj = EntrepreneurPortfolio.objects.get(user = request.user)
    form = EntrepreneurPortfolioForm(initial = model_to_dict(obj))
    if request.method == 'POST':
        form = EntrepreneurPortfolioForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('/entrepreneurs/homepage/')
        else:
            print(form.errors)
            return render(request, 'entrepreneurs/error.html')
    context = {'form': form} 
    return render(request, 'entrepreneurs/portfolio.html', context)

@login_required
@user_passes_test(entrepreneur_check, login_url = '/')
def entrepreneur_homepage(request):
    """
    Renders the entrepreneur homepage with mini portfolios of investors, filter functionality not available
    yet. Sending all investor portfolios from the database as of now.
    """

    allInvestors = Investors.objects.all()
    context = {"Investors" : allInvestors}

    return render(request= request, template_name = "entrepreneurs/homepage.html", context = context)

@login_required
@user_passes_test(entrepreneur_check,login_url = '/')
def investor_slug(request,pk):
    """
    Renders the page for an invidividual investor portfolio, maybe we could figure out a better way instead of
    explicitly sending interest_list and options, they're already a part of variable investor.
    """

    investor = Investors.objects.get(pk=pk)
    context = {"investor" : investor}
    return render(request = request, template_name = "entrepreneurs/inv_slug.html",context = context)
