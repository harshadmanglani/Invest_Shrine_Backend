from django.shortcuts import render
from .forms import EntrepreneurForm

def register(request):
    form = EntrepreneurForm
    if request.method == 'POST': 
        print(request.POST) 
        form = EntrepreneurForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save() 
            return render(request, 'entrepreneurs/registration_successful.html')
        else:
            return render(request, 'entrepreneurs/error.html')
    context = {'form': form} 
    return render(request, 'entrepreneurs/registration.html', context)

# Create your views here.