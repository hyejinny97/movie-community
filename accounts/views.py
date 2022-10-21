from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:signup')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/signup.html',context)

def signin(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if form.is_valid():
        login(request, form.get_user())
        return redirect('accounts:index')

    return render(request, 'accounts/signin.html', {"form": form})

def signout(request):
    logout(request)
    return redirect("accounts:index")