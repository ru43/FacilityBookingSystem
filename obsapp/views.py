from django.shortcuts import render,redirect
from django.urls import path
from django.http import HttpResponse
from .models import *
from .forms import *
from .signals import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group

@login_required(login_url='login')
# @allowed_users(allowed_roles=['user'])
def home(request):
    # books=request.user.customer.book_set.all()
    # context={'books':books}
    return render(request,'land.html')
@admin_only
def adminPage(request):
    bookings=Book.objects.all()
    customer=Customer.objects.all()
    context={ 'bookings':bookings }
    return render(request,'adminpage.html',context)


def userDetails(request):
    customer=Customer.objects.all()

    context={'customer' : customer}
    return render(request,'userdetails.html',context)

@login_required(login_url='login')
def cse(request):
    return render(request,'cse.html')

@unauthenticated_user
def login_page(request):
    if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

def register(request):
    form=CreateUserForm()
    if request.method =='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request , 'account created')
            return redirect("login")
    context={'form':form}
    return render(request,'register.html',context)


def bookfacility(request):
    form = BookForm()
    context={'form':form}
    if request.method=='POST':
        # print('printing post',request.POST)
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'book.html',context)


def deleteBooked(request,pk):
    book=Book.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('adminp')
    context={'book':book}
    return render(request ,'delete.html',context)


def bookings(request,pk):
    book=Book.objects.get(id=pk)
    context={'books':books}
    return render(request,'bookings.html',context)
