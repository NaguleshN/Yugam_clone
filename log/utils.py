from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client():
    subject="new message"
    message=" hello world "
    from_email= settings.EMAIL_HOST_USER
    recipient_list=["nagulesh03@gmail.com"]
    
    # send_mail( settings.EMAIL_HOST_USER, message ,from_email ,recipient_list,fail_silently=False)
    send_mail(
            "Product ordered by ",
            "A product from our bakery has been ordered. Address: . Zip code: . Phone: ",
            
            ["nagulesh03@gmail.com"],
            fail_silently=False,
        )