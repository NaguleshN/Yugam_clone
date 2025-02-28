from .views import login_view
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView ,PasswordChangeDoneView
from django.urls import reverse_lazy

urlpatterns = [
    
    path('login/', login_view, name='login'),
    path("",views.home,name='home'),
    path("hello/",views.send_email,name='send_email'),
    path('profile/', views.profile, name='profile'),
    path('pro_show/', views.pro_show, name='pro_show'),
    path('reg_details/', views.reg_details, name='reg_details'),
    path('register/', views.register, name='register'),
    path("room_booking/",views.room_booking,name='room_booking'),
    path("eventlist/",views.eventlist,name='eventlist'),
    path("workshop/",views.workshop,name='workshop'),
    path("ordering/<int:sno>",views.order,name='order'),
    path("booking/<int:select>",views.booking,name='booking'),
    path('change_password/', views.change_password, name='change_password'),
    path("logout",views.logout_view),
    path("add_event/",views.add_event,name="add_event"),
    path("update/<int:pk>",views.update,name="update"),
    path("events_enrolled/",views.events_enrolled,name='events_enrolled'),
    path("delete/<str:pk>",views.delete,name="delete"),
    path("delete_event/<int:pk>",views.delete_event,name="delete_event"),
    path("delete_workshop/<int:pk>",views.delete_workshop,name="delete_workshop"),
    path("<str:ev>/",views.event_disp, name= "e"),
    path("registered successfull/<str:name>/<int:identify>",views.reg_success,name='reg_success'),
    path("cancelled successfull/<str:name>",views.cancel_success,name='cancel_success'),
    
]