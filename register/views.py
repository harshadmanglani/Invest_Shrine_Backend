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
from investors.models import parse as parseinvestorportfolio
#in order to perform login and logout we will use these inbuilt django functions


def logout_request(request): # process logout request
    logout(request)
    messages.info(request,"You have successfully logged out ")
    return redirect("/") # returning to the homepage which is yet to be build, that's why showing runtime error

def homepage(request):
    return render(request = request, template_name = "register/landing_page.html")

def login_request(request): # process login request
#     """
#     Configure this functionality to be linked with the table.
#     """
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # if str(user.category) == 'Investor':
#                     request.session['investor_uid'] = str(user.id)
#                     return redirect('/investors/homepage/')

#                 elif str(user.category) == 'Entrepreneur':
#                     request.session['entrepreneur_uid'] = str(user.id)
#                     return redirect('/entrepreneurs/homepage/')
               
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    context  = {"form" : form}

    return render(request = request, template_name = "register/login.html", context = context)

def investor_register(request):
    if request.method == 'POST':
        user_form = NewUserForm(request.POST, prefix = 'UF')
        # portfolio_form = InvestorPortfolioForm(request.POST,prefix ='PF')
        
        if user_form.is_valid():
            user = user_form.save(commit=False)      
            user.save()
            # print(request.user)
            login(request,user)
            messages.info(request,f"You are now logged in as : {user_form.cleaned_data.get('username')}")
            return redirect('/investors/portfolio/')
            
            # parseinvestorportfolio(user, portfolio_form)

            # user.investor_portfolio.save()

    else:
        user_form = NewUserForm(prefix='UF')
        # portfolio_form = InvestorPortfolioForm(prefix='PF')


    context ={
            'user_form': user_form,
            # 'portfolio_form': portfolio_form,
        }
    return render(request= request, template_name='register/investor_register.html',context =context)

	
def entrepreneur_register(request):
    if request.method == 'POST':
        user_form = NewUserForm(request.POST, prefix = 'UF')
        portfolio_form = EntrepreneurPortfolioForm(request.POST,prefix ='PF')
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)      
            user.save()
            
            parseentrepreneurportfolio(user, portfolio_form)

            user.investor_portfolio.save()

    else:
        user_form = NewUserForm(prefix='UF')
        portfolio_form = EntrepreneurPortfolioForm(prefix='PF')


    context ={
            'user_form': user_form,
            'portfolio_form': portfolio_form,
        }
    return render(request= request, template_name='register/investor_register.html',context =context)

    
def about(request):
    return render(request=request, template_name = "register/about.html") 

def contact_us(request):
    return render(request = request,template_name = "register/contact.html")


    