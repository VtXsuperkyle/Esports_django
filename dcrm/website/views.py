from django.shortcuts import render,redirect
from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'website/index.html')

#register a user
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')

    context = {'form': form}

    return render(request,'website/register.html', context=context)

#login
def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('infopage')

    context = {'login_form':form}
    return render(request,'website/my-login.html', context=context)


#logout user
def logout(request):
    auth.logout(request)
    return render(request,'website/logout.html')

#dashboard
def infopage(request):
    return render(request, 'website/infopage.html')

#account
def account(request):
    return render(request, 'website/account.html')