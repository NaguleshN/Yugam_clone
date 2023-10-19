from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PasswordChangeForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import RegistrationForm
from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .models import varieties

# from login_auth import templates

# Create your views here.
# from log.forms import YourForm

def pin_check(s):
    
    l, u, p, d = 0, 0, 0, 0
    # s = "N@gu_leSh03$"
    if (len(s) >= 8):
        for i in s:
        # counting lowercase alphabets
            if (i.islower()):
                l+=1           
        # counting uppercase alphabets
            if (i.isupper()):
                u+=1           
        # counting digits
            if (i.isdigit()):
                d+=1           
        # counting the mentioned special characters
            if(i=='@'or i=='$' or i=='_'):
                p+=1          
        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
            print("Valid Password")
            return True    
        else:
            return False
  

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password1']

            # Check if the old password matches the current user's password
            if not request.user.check_password(old_password):
                messages.error(request, "The old password is incorrect.")
                # Update the user's password
                if pin_check(new_password)==True:
                    request.user.set_password(new_password)
                    request.user.save()
                    messages.success(request, "Password changed successfully.")
                    return redirect('home')   
            else:
                messages.error(request, "The password should contains capital,small letters,digits and some special characters.")
                form = PasswordChangeForm()
    else:
        form = PasswordChangeForm()
    return render(request, 'registration/password_change.html', {'form': form,"is_admin":isadmin(request)})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if pin_check(password)==True:
                user = User.objects.create_user(username=username, email=email, password=password)
                return redirect('home')  # Redirect to a profile page or any other page
            else:
                messages.error(request, "The password should contains capital,small letters,digits,special chars[@,_,/'/'] ")
                pass
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form,"is_admin":isadmin(request)})

@login_required
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or perform other actions
                return redirect('success_page')
            else:
                # Handle invalid login credentials
                pass
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form,"is_admin":isadmin(request)})

@login_required
def profile(request):
    if request.method=="POST":
        name=request.POST.get('name')
        try:
            user = User.objects.get(username=name)
            em =user.email
        except:
            em=request.POST.get('email')
        gen=request.POST.get('gender')
        mob=request.POST.get('mobile')
        clg=request.POST.get('college')
        yr=request.POST.get('year')
        ename=request.POST.get('event_name')
        
        Profile.objects.create(user=User,name=name,gender=gen,email_address=em,mobile=mob,college=clg,year_of_study=yr)
        
    reg=Event.objects.all()
    prof=Profile.objects.all()
    return render(request,"options/profile.html",{'reg':reg,"is_admin":isadmin(request),"profile":prof})    

def home(request): 
    return render(request,'home.html',{"is_admin":isadmin(request)})

@login_required
def isadmin(request):
    if request.user.is_superuser:
        is_admin="1"
    else:
        is_admin=0
    return is_admin
    
@login_required
def pin_change(request):
    return render (request,'registration/password_change_form.html',{"is_admin":isadmin(request)})
@login_required
def room_booking(request):
    return render(request,"options/room_accomadation.html",{"is_admin":isadmin(request)})
@login_required
def eventlist(request):
    variety=varieties.objects.all()
    events=Event.objects.all()
    print(events)
    
    return render (request,"options/competitions.html",{'events':events,'variety':variety,"is_admin":isadmin(request)})

@login_required
def event_disp(request,ev):
    events=Event.objects.all()
    workshop=Workshop.objects.all()
    print(ev)
    for i in events:
        if i.event_name==ev:
            return render(request,"event_display.html",{"events":events,"ev":ev,"is_admin":isadmin(request)})
    for j in workshop:
        if j.workshop_name==ev:
            return render(request,"event_display.html",{"workshop":workshop,"ev":ev,"is_admin":isadmin(request)})
        
@login_required
def logout_view(request):
    logout(request)
    return redirect("/")
@login_required
def add_event(request):
    if request.method=="POST":
        event_name=request.POST.get("event_name")
        instruction=request.POST.get("instruction")
        cat=request.POST.get("cat")    
        category=varieties.objects.get(type_name=cat)
        date=request.POST.get("date")
        mode=request.POST.get("mode")
        registration_fee=request.POST.get("reg_fees")
        prize_amount=request.POST.get("prize")
        contact_number=request.POST.get("contact_no")
        duration=request.POST.get("duration")
        venue=request.POST.get("venue")
        Event.objects.create(event_name=event_name,instruction=instruction,category=category,date=date,mode=mode,registration_fee=registration_fee,prize_amount=prize_amount,contact_number=contact_number,duration=duration,venue=venue)
    var=varieties.objects.all()
    events=Event.objects.all()
    return render(request,"add_event.html",{"is_admin":isadmin(request),"category":var})  

@login_required
def workshop(request):
    variety=varieties.objects.all()
    workshop=Workshop.objects.all()
    print(workshop)
    
    return render (request,"options/workshop.html",{'workshop':workshop,'variety':variety,"is_admin":isadmin(request)})

@login_required
def reg_success(request,id):
    
    workshop=Workshop.objects.all()
    events=Event.objects.all()
    for i in workshop:
        if i.id==id:  
            print(i) 
            registeration.objects.create(user=request.user,event_or_workshop=i)       
            return render (request,"reg_suc.html",{'events':i,"is_admin":isadmin(request)})
    
    for j in events:
        if j.id==id:  
            print(j)
            registeration.objects.create(user=request.user,event_or_workshop=j)       
            return render (request,"reg_suc.html",{'events':j,"is_admin":isadmin(request)})
