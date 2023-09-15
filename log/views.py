from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

# from login_auth import templates

# Create your views here.

    
def prof(request):
    if request.method=="POST":
    
        name=request.POST.get('name')
        em=request.POST.get('email')
        gen=request.POST.get('gender')
        mob=request.POST.get('mobile')
        clg=request.POST.get('college')
        yr=request.POST.get('year')
        ename=request.POST.get('event_name')

        register.objects.create(name_of_the_candidate=name,email_address=em,gender=gen,mobile=mob,college=clg,year_of_study=yr,events_name=ename)
        
    reg=Event.objects.all()
    return render(request,"options/event_registration.html",{'reg':reg})    
            
    
def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=UserCreationForm()       
    return render(request,'registration/signup.html',{
        'form':form
    })


def home(request):
    # count=User.objects.count()
    # 'count':count
    return render(request,'home.html')

def pin_change(request):
    return render (request,'registration/password_change_form.html')

def room_booking(request):
    return render(request,"options/room_accomadation.html")
def eventlist(request):
    variety=varieties.objects.all()
    events=Event.objects.all()
    print(events)
    # a=varieties.type_no.all()
    # print(events)
    # context={
    #     'event_no':events,
    #     'event_name':varieties.objects.get(type_name="Cultural"),
    # }
    return render (request,"options/competitions.html",{'events':events,'variety':variety})


def eventdisp(request,ev):
    events=Event.objects.all()
    print(ev)
    return render(request,"event_display.html",{"events":events,"ev":ev})

def logout_view(request):
    logout(request)
    return redirect("/")