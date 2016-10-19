from django.shortcuts import render, redirect, HttpResponse
from .models import User

# Create your views here.

def index(request):
    return render(request, 'email_Val/index.html')

def add(request):
    if request.method == 'POST':
        result = User.objects.validate(request.POST['email'])
        if result == True:
            User.objects.create(email = request.POST['email'])
            print True
            return redirect('/success')
        else:
            return redirect('/')

def success(request):
    context = {
        'users' : User.objects.all()
    }
    print User.objects.all()
    return render(request, 'email_Val/success.html', context)
