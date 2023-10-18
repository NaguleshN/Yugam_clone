from .views import login_view
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView ,PasswordChangeDoneView
from django.urls import reverse_lazy

urlpatterns = [
    
    path('login/', login_view, name='login'),
    path("",views.home,name='home'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path("room_booking/",views.room_booking,name='room_booking'),
    path("eventlist/",views.eventlist,name='eventlist'),
    path("workshop/",views.workshop,name='workshop'),
    path('change_password/', views.change_password, name='change_password'),
    path("logout",views.logout_view),
    path("add_event/",views.add_event,name="add_event"),
    path("<str:ev>/",views.event_disp, name= "e"),
    path("registered successfull/<int:id>",views.reg_success,name='reg_suc'),
   
]