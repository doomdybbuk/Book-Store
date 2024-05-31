from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import  HttpResponse
from django.contrib.auth import authenticate, login as auth_login


def welcome(request):
    return render(request,'welcome.html')
def signup(request):
    if request.method == 'POST':
        uname = request.post.get('username')
        email = request.post.get('email')
        pass1 = request.post.get('password')
        conf_pass = request.post.get('confirm_password')
        if pass1 != conf_pass:
            return HttpResponse("Password does not match")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        user1 = request.POST.get("user");
        pass2 = request.POST.get("pass2")
        user = authenticate(request,user1=user,pass1=pass2)
        if user is not None:
            auth_login(request,user)
            return redirect('home.html')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def profile(request):
    return HttpResponse("This is the profile page")