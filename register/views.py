from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from django.contrib import messages
#in order to perform login and logout we will use these inbuilt django functions


def logout_request(request): #process logout request
    logout(request)
    messages.info(request,"You have successfully logged out ")
    return redirect("/") # returning to the homepage which is yet to be build, that's why showing runtime error


def homepage(request):
    return render(request = request, template_name = "register/landing_page.html")

def login_request(request):
   
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                #return redirect('/')#returning to the homepage which is yet to be build, that's why showing runtime error
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    context  = {"form" : form}

    return render(request = request, template_name = "register/login.html", context = context)

def register(request):
    
    #following code will handle POST requests
    if request.method == 'POST':
        print("POST method initiated")
        form = NewUserForm(request.POST)
        if form.is_valid():
            print("valid")
            user = form.save()
            username = form.cleaned_data.get('username')
            #displays messages, inbuilt library in django
            messages.success(request,f"New Account Created : {username}")
            login(request,user)
            messages.info(request,f"You are now logged in as : {username}")

            return redirect('/')
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg} : {form.error_messages[msg]}")

    context = {"form"  : NewUserForm}
    return render(request = request, template_name = "register/register.html",context = context)



def about(request):
    return render(request=request, template_name = "register/about.html") 

def contact_us(request):
    return render(request = request,template_name = "register/contact.html")


    