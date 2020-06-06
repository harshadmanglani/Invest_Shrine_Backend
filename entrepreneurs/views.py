from django.shortcuts import render
from .forms import *
from investors.models import Portfolio as Investors

def portfolio(request):
    form = EntrepreneurPortfolioForm
    if request.method == 'POST': 
        print(request.POST) 
        form = EntrepreneurPortfolioForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, 'entrepreneurs/successful.html')
        else:
            return render(request, 'entrepreneurs/error.html')
    context = {'form': form} 
    return render(request, 'entrepreneurs/portfolio.html', context)

#def landing_page(request):
 #   return render(request, 'entrepreneurs/landing_page.html')



def entrepreneur_homepage(request):
    allInvestors = Investors.objects.all()
    context = {"Investors" : allInvestors}

    return render(request= request, template_name = "entrepreneurs/homepage.html", context = context)

def investor_slug(request,pk):
    investor = Investors.objects.get(pk=pk)
    context = {"details" : investor}
    return render(request = request, template_name = "entrepreneurs/inv_slug.html",context = context)
