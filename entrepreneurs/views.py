from django.shortcuts import render
from .forms import *


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

def landing_page(request):
    return render(request, 'entrepreneurs/landing_page.html')


# Create your views here.