from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
#in order to perform login and logot we will use these inbuilt django functions


def logout_request(request): #process logout request
    logout(request)
    return redirect("/") # returning to the homepage which is yet to be build, that's why showing runtime error


def homepage(request):
    return HttpResponse("This is the homepage")

def login_request(request):
   
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #messages.info(request, f"You are now logged in as {username}")
                return redirect('/')#returning to the homepage which is yet to be build, that's why showing runtime error
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    context  = {"form" : form}

    return render(request = request, template_name = "login.html", context = context)

    