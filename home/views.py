from django.shortcuts import render,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def loginuser(request):
 if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        print(username,password)

        if user is not None:
            login(request,user)
            return redirect("userAccount/")
        else:
            messages.warning(request,'Invalid Credentials.')
            return render(request,'login.html')
 return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        if User.objects.filter(username=name).exists():
            messages.warning(request, 'Username Already taken')
            return render(request,'signup.html')
        elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exists')
                return render(request,'signup.html')
        else:
            if(password1==password2 and len(password1)>=8):
                  registered_user=User.objects.create_user(username=name,password=password1,email=email)
                  registered_user.save()
                  messages.success(request, 'SignUp successful')
                  return redirect('/login')
            else:
                 messages.warning(request, 'Your password doesnot match or too short')
                 return render(request,'signup.html')
    else:

       return render(request,'signup.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')

def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, 'Your Message has been received.')
    return render(request,'contact.html')
