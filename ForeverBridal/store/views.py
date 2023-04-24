from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from mysite.core.forms import SigninForm


def index(request):
    return render (request, 'index.html')

def login(request):
    return render (request, 'login.html')


def signin(request):
    form = S
    if request.method == 'POST':
        form = signin(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = signin()
    return render(request, 'signup.html', {'form': form})

def forget_password(request):
    return render (request, 'forget-password.html')

def contact(request):
    return render (request, 'contact.html')

def dress(request):
    return render (request, 'dress.html')
    
def manSuit(request):
    return render (request, 'manSuit.html') 
   
def accessories(request):
    return render (request, 'accessories.html')

def manAccessories(request):
    return render (request, 'manAccessories.html')

def earring(request):
    return render (request, 'earring.html')


# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login

# from .forms import ConnexionForm

# def connexion(request):
#     if request.method == 'POST':
#         form = ConnexionForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect.")
#     else:
#         form = ConnexionForm()
#     return render(request, 'connexion.html', {'form': form})
