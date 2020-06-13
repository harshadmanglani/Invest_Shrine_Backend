from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from django.contrib import messages
from investors.models import Portfolio as InvestorPortfolio
from entrepreneurs.models import PortfolioEnt as EntrepreneurPortfolio
from investors.forms import InvestorPortfolioForm as InvestorPortfolioForm
from entrepreneurs.forms import EntrepreneurPortfolioForm as EntrepreneurPortfolioForm
from .models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.decorators import login_required


def logout_request(request): # process logout request
    if not request.user.is_authenticated:
        return redirect('/')
    logout(request)
    messages.info(request,"You have successfully logged out ")
    return redirect("/") 

def homepage(request):
    return render(request = request, template_name = "register/landing_page.html")
    
@login_required
def portfolio(request):
    if request.user.category == 'Investor':
        print('Rendering investor portfolio')
        return redirect('/investors/portfolio')
    
    elif request.user.category == 'Entrepreneur':
        print('Rendering entrepreneur portfolio')
        return redirect('/entrepreneurs/portfolio')

def login_request(request): # process login request
    """
    Configure this functionality to redirect to separate homepages
    """
    if request.user.is_authenticated:
        return redirect(request.GET.get('next', '/'))
        
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next', None) is not None:
                    return redirect(request.GET['next'])
                else:
                    if user.category == 'Investor':
                        return redirect('/investors/homepage')
                    elif user.category == 'Entrepreneur':
                        return redirect('/entrepreneurs/homepage')
                    else:
                        pass
               
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    context  = {"form" : form}

    return render(request = request, template_name = "register/login.html", context = context)

def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        user_form = NewUserForm(request.POST, prefix = 'UF')
        
        if user_form.is_valid():
            user = user_form.save(commit=False)      
            user.save()
            login(request,user)
            messages.info(request,f"You are now logged in as : {user_form.cleaned_data.get('username')}")
            if user.category == 'Investor':
                return redirect('/investors/portfolio')
            elif user.category == 'Entrepreneur':
                return redirect('/entrepreneurs/portfolio')
            else: pass
            
    else:
        user_form = NewUserForm(prefix='UF')

    context ={
            'form': user_form,
        }
    return render(request= request, template_name='register/register.html',context =context)
    
def about(request):
    return render(request=request, template_name = "register/about.html") 

def contact_us(request):
    return render(request = request,template_name = "register/contact.html")


    