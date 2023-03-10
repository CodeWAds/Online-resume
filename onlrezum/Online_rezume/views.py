from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, LoginUserForm
from django.http import HttpResponse


def privacy(request):
    return render(request, 'Online_rezume/html/Privacy.html')

def sign_in(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user is not None:
                login(request,user)
                return redirect('/pers_area')
            else:
                form.add_error(None, 'Invalid username or password')
                return redirect('/sign_in')       
          
    else:
            form = LoginUserForm()

            context = {'form': form}
            return render(request, 'Online_rezume/html/Auth.html', context)


def pers_area(request):
    return render(request, 'Online_rezume/html/Pers_area.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect ("/pers_area")
    else:
         form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'Online_rezume/html/Sign_up.html', context)
    