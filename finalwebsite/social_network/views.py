from django.shortcuts import render,redirect
from .models import user
import hashlib
from .validation import validation_check
from .forms import Signup
def signup(request):
    #form=Signup()
    return render(request,'signup.html',{'msg':''})
def login(request):
    return render(request, 'login.html', {'msg': ''})

def save(request): #for signup details and login
    if request.method=="POST":
        if request.POST.get("submit")=='Sign Up':
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            raw_password = request.POST.get("password")
            temp_password = hashlib.md5(raw_password.encode())
            password = temp_password.hexdigest()

            z=validation_check(name,phone,email)

            if z.get('Name') != 'Valid' or z.get('Phone') != 'Valid' or z.get('Email') != 'Valid':
                return render(request,'signup.html', {'msg': 'Invalid input'})
            if user.objects.filter(phone=phone):
                return render(request,'signup.html',{'msg': 'phone no. already registered'})
            insert = user(name=name, phone=phone, email=email, password=password)
            insert.save()
            return render(request, 'homepage.html', )

        elif request.POST.get("submit")=='Log In':
            phone = request.POST.get("phone")
            raw_password = request.POST.get("password")
            temp_password = hashlib.md5(raw_password.encode())
            password = temp_password.hexdigest()
            if user.objects.filter(phone=phone):
                x = user.objects.filter(phone=phone)
                temp = (list(x)[0]).password
                if password == temp:
                    return render(request, 'homepage.html',)
                else:
                    return render(request, 'login.html', {'msg': 'wrong password'})
            else:
                return render(request, 'login.html', {'msg': 'invalid credentials'})