from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact_us.html')