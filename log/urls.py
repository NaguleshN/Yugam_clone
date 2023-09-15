
from django.urls import path
from . import views

urlpatterns = [
    # path("",views.home,name="hello"),
    path("signup/",views.signup,name='signup'),
    path("",views.home,name='home'),
    # path("login/",views.login_user,name='login'),
    path("password_change/",views.pin_change,name='password_change'),
    path("room_booking/",views.room_booking,name='room_booking'),
    path("eventlist/",views.eventlist,name='eventlist'),
    # path("disp/",views.disp,name="disp"),
    path("registration/",views.prof,name="registering"),
    path("logout",views.logout_view),
    
    path("<str:ev>/",views.eventdisp, name= "e")
   
    
    
    
]