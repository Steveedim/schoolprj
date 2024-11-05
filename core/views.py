from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, UserLoginForm

# Create your views here.
def home(request):
    context = {}
    return render(request, 'core/home.html', context)

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('core:home')
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'core/login.html', context)

def signup(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:home")

    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, "core/signup.html", context)
