from django.shortcuts import render,redirect
from application.models import product
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
def home(request):
    fruits=product.objects.filter(categories='fruits')
    veg=product.objects.filter(categories='vegetables')
    dry=product.objects.filter(categories='DRY FRUITS')
    snack=product.objects.filter(categories='SNACKS')
    oil=product.objects.filter(categories='Oils')
    cool=product.objects.filter(categories='COOL DRINKS')
    
    rating=[1,2,3,4,5]
    return render(request,'home.html',{'fruits':fruits,'veg':veg,'dry':dry,'snack':snack,'oil':oil,'cool':cool,'rating':rating})




def show(request,id,categories):
    single=product.objects.get(id=id)
    below=product.objects.filter(categories=categories)
    
    rating=range(1,6)
    return render(request,'show.html',{'single':single,'below':below,'rating':rating})

def cart_list(request,id):
    cart=request.session.get('store',[])
    if id not in cart:
        cart.append(id)
        request.session['store']=cart
    print(cart)
    return redirect('home')

def show_cart(request):
    cart=request.session.get('store',[])
    showlist=product.objects.filter(id__in=cart)
    store=[1,2,3,4,5]
    return render(request,'cart.html',{'showlist':showlist,'store':store})
def remove_cart(request,id):
    cart=request.session.get('store',[])
    cart.remove(id)
    request.session['store']=cart
    return redirect('show_cart')

def login1(request):
    return render(request,'login.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register1(request):
    if request.method == "POST":
        Username = request.POST.get('username')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        Confirm_Password = request.POST.get('confirm_password')
        Address=request.POST.get('address')
        Phonenumber=request.POST.get('phonenumber')
        
        # Check for empty fields
        if not Username or not Email or not Password or not Confirm_Password:
            messages.error(request, 'All fields are required')
            return redirect('register1')

        if Password != Confirm_Password:
            messages.error(request, 'Passwords do not match')
            return redirect('register1')

        if User.objects.filter(username=Username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register1')

        if User.objects.filter(email=Email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register1')

        # Create new user
        User.objects.create_user(username=Username, email=Email, password=Password)
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login1')

    return render(request, 'register.html')

from django.contrib import messages, auth
def login1(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        
        if user:
            auth.login(request, user)
            request.session['username'] = username
            request.session['password']=password
            messages.success(request, 'Login successful')
            return redirect("home")
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login1')
    return render(request, "login.html")

                
   
    

def filter_data(request):
    if request.method=="POST":
        query=request.POST.get('query',' ')
        
        try:
            single=product.objects.get(name=query)
            below=product.objects.filter(categories=single.categories)
        except:
            return render(request,'a.html')
        return render(request,'show.html',{'single':single,'below':below})
    
    
def categories(request,categories):
    below=product.objects.filter(categories=categories)
    return render(request,'show.html',{'below':below})

def order1(request):
    return render (request,'order.html')


def pay1(request,id):
    name=request.session.get('username')
    phonenumber=request.session.get('phonenumber')
    ab=product.objects.get(id=id)
    return render(request,'pay.html',{'name':name, 'phonenumber': phonenumber,"ab":ab})