# from log.utils import send_email_to_client
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PasswordChangeForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import RegistrationForm
from django.shortcuts import render,redirect
from django.db.models import Q

from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import logout
from django.contrib.auth.models import User , Group
from django.contrib import messages
from .models import *
from .models import varieties

print(Group)




def pin_check(s):
    
    # l, u, p, d = 0, 0, 0, 0
    # # s = "N@gu_leSh03$"
    # if (len(s) >= 8):
    #     for i in s:
    #     # counting lowercase alphabets
    #         if (i.islower()):
    #             l+=1           
    #     # counting uppercase alphabets
    #         if (i.isupper()):
    #             u+=1           
    #     # counting digits
    #         if (i.isdigit()):
    #             d+=1           
    #     # counting the mentioned special characters
    #         if(i=='@'or i=='$' or i=='_'):
    #             p+=1          
    #     if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
    #         print("Valid Password")
    #         return True    
    #     else:
    #         return False
    return True

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
    prof=Profile.objects.all()
    print(prof)
   
    reg=Event.objects.all()
    
    if request.method=="POST":
        name=request.POST.get('name')
        try:
            user = User.objects.get(username=name)
        except:
            pass
        em=request.POST.get('email')
        gen=request.POST.get('gender')
        mob=request.POST.get('mobile')
        clg=request.POST.get('college')
        yr=request.POST.get('year')
        
        Profile.objects.create(user=request.user,name=name,gender=gen,email_address=em,mobile=mob,college=clg,year_of_study=yr)
        
    prof=Profile.objects.all()
    not_found=0
    for i in prof :
        print("hello")
        print(i.user)
        print(request.user)
        if i.user == request.user:
            print(i.user)
            not_found=0 
            print(not_found)
            break     
        else:
            not_found=1
            print(not_found)   
    return render(request,"options/profile.html",{'reg':reg,"is_admin":isadmin(request),"profile":prof ,"not_found":not_found})    

@login_required
def update(request ,pk):
    reg=Event.objects.all()
    prof=Profile.objects.all()
    
    if request.method=="POST":
    
        for i in prof:
            if i.pk==pk:   
                Profile.objects.filter(pk=pk).delete()
        Profile.objects.filter(user=request.user).delete()    
        name=request.POST.get('name')
        try:
            user = User.objects.get(username=name)
        except:
            pass
        em=request.POST.get('email')
        gen=request.POST.get('gender')
        mob=request.POST.get('mobile')
        clg=request.POST.get('college')
        yr=request.POST.get('year')
        ename=request.POST.get('event_name')
        
        Profile.objects.create(user=request.user,name=name,gender=gen,email_address=em,mobile=mob,college=clg,year_of_study=yr)
        return redirect("profile")
    return render(request,"crud/update.html",{'reg':reg,"is_admin":isadmin(request),"profile":prof,'id':pk})
       
@login_required
def delete(request,pk):
    prof=Profile.objects.all()
    if request.method=="POST":
        for i in prof:
            print(i.pk)
            if i.pk==pk:   
                Profile.objects.filter(id=pk).delete()
    Profile.objects.filter(pk=pk).delete()
    return redirect("profile")
            
def home(request): 
    return render(request,'pro_show.html',{"is_admin":isadmin(request)})


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
    reg=registeration.objects.all()
    print(ev)
    t=0
    for i in events:
        print(i)
        if i.event_name==ev:
            print(ev)
            for j in reg:
                if j.user==request.user:
                    if j.event_or_workshop==i.event_name:
                        t=1
            print("hello")
            return render(request,"event_display.html",{"events":events,"ev":ev,"is_admin":isadmin(request),"check":t})
    for j in workshop:
        print(j)
        if j.workshop_name==ev:
            for i in reg:
                if i.user==request.user:
                    if i.event_or_workshop==j.workshop_name:
                        t=1
            return render(request,"event_display.html",{"workshop":workshop,"ev":ev,"is_admin":isadmin(request),"check":t})
    return redirect("/")    
@login_required
def logout_view(request):
    logout(request)
    return redirect("/")
@login_required
def add_event(request):
    ev=Event.objects.all()
    if request.method=="POST":
        for j in ev:
            
            print(j.event_name)
            if  j.event_name == request.POST.get("event_name") :
                messages.error(request,"event already exists")
                return redirect("add_event")
                
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
        messages.success(request, f"You have successfully added { event_name } ")
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
def cancel_success(request,name):  
    workshop=Workshop.objects.all()
    events=Event.objects.all()
    prof=Profile.objects.all()
    reg=registeration.objects.all()
    if name =="workshop":
        for i in workshop:
            for k in reg:
                if request.user==k.user:
                    n=k.user
                    if k.event_or_workshop== i.workshop_name:
                        print("deleted")
                        registeration.objects.filter(Q(user = k.user) & Q(event_or_workshop = i.workshop_name)).delete() 
                        print(i)
                        return render(request,"cancel_suc.html",{"events":i.workshop_name})
                
    if name=="event":
        for j in events:
            print(j)
            for k in reg:
                if request.user==k.user:
                    n=k.user
                    if k.event_or_workshop== j.event_name:
                        print("deleted")
                        registeration.objects.filter(Q(user = k.user) & Q(event_or_workshop = j.event_name)).delete() 
                        print(j)
                        return render(request,"cancel_suc.html",{"events":j.event_name})

    return render(request,"cancel_suc.html")


@login_required
def reg_success(request,name,identify):
    
    workshop=Workshop.objects.all()
    events=Event.objects.all()
    prof=Profile.objects.all()
    reg=registeration.objects.all()
    check=0
    for n in prof:
        if request.user == n.user:
            print(request.user)
            print(n.user)
            check=1
            for i in workshop:
                print(name)
                if name=="workshop":  
                    if i.id == identify:  
                        for k in reg:
                            print(k.user)
                            print(request.user)
                            if request.user == k.user :
                                if i.workshop_name==k.event_or_workshop: 
                                    # p=0 
                                    print("hello")
                                    return render (request,"reg_suc.html",{'events':i,"is_admin":isadmin(request),"p":0})
                        
                        registeration.objects.create(user=request.user,event_or_workshop=i)   
                        return render (request,"reg_suc.html",{'events':i,"is_admin":isadmin(request),"p":1})
                        break
            
            for j in events:
                print(name)
                if name == "event" :
                    print(j.id)
                    if j.id == identify:
                        p=0  
                        for k in reg:
                            if request.user == k.user :
                                if j.event_name==k.event_or_workshop: 
                                    print("hello")
                                    # p=0     
                                    return render (request,"reg_suc.html",{'events':j.event_name,"is_admin":isadmin(request),"p":0})
                        # p+=1     
                        registeration.objects.create(user=request.user,event_or_workshop=j.event_name)  
                        return render (request,"reg_suc.html",{'events':j.event_name,"is_admin":isadmin(request),"p":1})
                        break

    if check ==0:
        messages.error(request, "First create your profile to register")        
    return redirect("profile")   
        
        
@login_required
def reg_details(request):
    reg=registeration.objects.all()
    prof=Profile.objects.all()
    events=Event.objects.all() 
    workshop=Workshop.objects.all()
    if request.method=="POST":
        f=request.POST.get("filter")
        print(f)
        
        return render(request,"filter_disp.html",{"filter":f,"events":events,"workshop":workshop,"reg":reg,"is_admin":isadmin(request)})
        
    return render(request,"options/registered_details.html",{"reg":reg,"prof":prof,"events":events,"workshop":workshop,"is_admin":isadmin(request)})

def events_enrolled(request):
    events=Event.objects.all() 
    workshop=Workshop.objects.all()
    reg=registeration.objects.all()
    return render(request,"options/events_enrolled.html",{"reg":reg,"events":events,"workshop":workshop})




def send_email(request):

    email=EmailMessage(
        "Thanks for registration ",
        " Your tickets are ordered successfull . ",
        settings.EMAIL_HOST_USER,
        ["goutham172904@gmail.com"],     
    )
    email.fail_silently=False,
    email.send()
    return redirect("home")


def delete_event(request,pk):
    event=Event.objects.all()
    workshop=Workshop.objects.all()
    for i in event:
        if i.id == pk :
            Event.objects.filter(event_name=i.event_name).delete()
    return redirect("eventlist")
    
def delete_workshop(request,pk): 
    event=Event.objects.all()
    workshop=Workshop.objects.all()       
    for i in workshop:
        if i.id == pk:
            Event.objects.filter(workshop_name=i.workshop_name).delete()
    return redirect("workshop")    

def pro_show(request):  
    return render(request,"pro_show.html")

def booking(request,select):
   
    return render(request,"booking.html",{"select":select})

def order(request , sno):
    pro=proshow.objects.all()
    if request.method =="POST":
        # return render(request,"terms.html")
        send_email(request)
        return render (request,"reg_suc.html",{'events':"Concert","is_admin":isadmin(request),"p":1})
    return render(request,"order.html" ,{"sno":sno,"proshow":pro})