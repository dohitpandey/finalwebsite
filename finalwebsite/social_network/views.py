from django.shortcuts import render,redirect,HttpResponse
from .models import user,friends
import hashlib
from .validation import validation_check
from .forms import Signup
from django.template.defaultfilters import slugify

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
            password = request.POST.get("password")

            # temp_password = hashlib.md5(raw_password.encode())
            # password = temp_password.hexdigest()

            z=validation_check(name,phone,email)

            if z.get('Name') != 'Valid' or z.get('Phone') != 'Valid' or z.get('Email') != 'Valid':
                return render(request,'signup.html', {'msg': 'Invalid input'})
            if user.objects.filter(phone=phone):
                return render(request,'signup.html',{'msg': 'phone no. already registered'})
            if request.FILES.get('file') is not None:
                propic = request.FILES.get('file')
                insert = user(name=name, phone=phone, email=email, password=password, profile_pic=propic)
            else:
                insert = user(name=name, phone=phone, email=email, password=password)
            insert.save()
            request.session['id'] = user.objects.get(phone=phone).id
            friends.objects.create(lou=user.objects.get(phone=phone))
            return redirect('homepage')

        elif request.POST.get("submit")=='Log In':
            phone = request.POST.get("phone")
            password = request.POST.get("password")
            # temp_password = hashlib.md5(raw_password.encode())
            # password = temp_password.hexdigest()
            if user.objects.filter(phone=phone):
                x = user.objects.filter(phone=phone)
                temp = (list(x)[0]).password
                if password == temp:
                    request.session['id'] = user.objects.get(phone=phone).id
                    return redirect('homepage')
                else:
                    return render(request, 'login.html', {'msg': 'wrong password'})
            else:
                return render(request, 'login.html', {'msg': 'invalid credentials'})

def home(request):
    id=request.session.get('id')
    myprofile=friends.objects.get(lou__id=id)
    excluding_me = friends.objects.exclude(lou=myprofile.lou)
    excluding_meset={val.lou for val in excluding_me}
    frnds=myprofile.lof.all()
    frndset=set(frnds)
    suggestions=list( excluding_meset.symmetric_difference(frndset))

    data = {
        'frnds':frnds,
        'suggestions':suggestions,
    }
    if request.GET.get('name'):
        name=request.GET.get('name')
        data['userdetails'] = user.objects.filter(name__icontains=name)
        data['ok']=1
    return render (request,'homepage.html',data)
def friend(request):
    if request.method=="POST":
        userid=request.POST.get("submit")
        userobject=user.objects.get(id=userid)
        id=request.session.get('id')
        User = friends.objects.get(lou__id=id)
        User.lof.remove(userobject)
    return redirect('homepage')
def suggestions(request):
    if request.method=="POST":
        userid=request.POST.get("submit")
        userobject=user.objects.get(id=userid)
        id = request.session.get('id')
        User=friends.objects.get(lou__id=id)
        User.lof.add(userobject)
    return redirect('homepage')
def profile(request,slugname):
    userdetails=user.objects.get(nameslug = slugname)
    data={'userdetails' : userdetails}
    return render(request,'profile.html',data)