from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.cache import cache_control, never_cache
from django.shortcuts import render
from .models import Customer

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
@never_cache
def contact(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        uemail = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        query = Customer(name=uname,email=uemail,phoneNumber=phone,description=desc)
        query.save()
        messages.success(request,"Thank you for contacting us. We will reach you soon")
    return render(request, 'contact.html')
def handleindex(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        password1=request.POST.get("password1")
        myuser=authenticate(username=uname,password=password1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Logged in Successfully")
            return redirect('/home')
        else:
            messages.error(request,"Username or password is incorrect")
            return redirect('/')
        
    return render(request,'index.html')

def handlesignup(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        Email=request.POST.get("email")
        password=request.POST.get("password1")
        confirmpassword=request.POST.get("password2")
        # print(uname,email,password,confirmpassword)
        if password != confirmpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/signup')
        try:
            if User.objects.get(username=uname):
                messages.info(request,"Username already exist")
                return redirect('/signup')
        except:
            pass
        try:
            if User.objects.get(email=Email):
                messages.info(request,"Email already exist")
                return redirect('/signup')
        except:
            pass
        myuser=User.objects.create_user(uname,Email,password)
        myuser.save()
        messages.success(request,"Signup Successfull. Please Login!")
        return redirect('/')
    return render(request,'signup.html')

def home(request):
    return render(request,'home.html')


def handlelogout(request):
    logout(request)
    messages.info(request,"logged out successfully")
    return redirect('/')