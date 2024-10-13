from django.shortcuts import render,redirect
from .models import Product
from .forms import SignUpForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

def base(request):
    return render(request, 'base.html')
def login_user(request):
    if request.method== 'POST':
        username = request.POST['username']
        password =request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'username or password is incorrect')
    return render(request, 'login.html')
    
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method=="POST":
       form=SignUpForm(request.POST)
       if form.is_valid():
        form.save()
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        email=form.cleaned_data['email']
        user=authenticate(username=username, password=password, email=email)
        login(request, user)
        messages.success(request, 'Account Was Created Successfully')
        return redirect ('/')
    else:
        form=SignUpForm()
    return render(request, 'signup.html', {'form':form})

def product_list(request):
    return render(request, 'product.html')

# Product Detail View
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
# Create your views here.
   
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
