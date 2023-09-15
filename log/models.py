from django.db import models

# Create your models here.

class varieties(models.Model):
    type_no=models.IntegerField()
    type_name=models.CharField(max_length=10)
    def __str__(self):
        return self.type_name
    
mode_choice=(('online','online'),('offline','offline'))
class Event(models.Model):
    event_name=models.CharField( max_length=20)
    instruction=models.CharField(max_length=1000)
    category=models.ForeignKey(varieties,on_delete=models.CASCADE)
    date=models.DateField()
    mode=models.CharField( max_length=10,  choices=mode_choice)
    registration_fee=models.IntegerField()
    prize_amount=models.IntegerField()
    contact_number=models.BigIntegerField()
    duration=models.DurationField()
    venue=models.CharField(max_length=50)
  
gender_choice=(("male","male"),("female","female"))  
year_option=(("year 1","First year"),("year 2","Second year"),("year 3","Third year"),("year 4","Final year"))

class register(models.Model):
    name_of_the_candidate=models.CharField(max_length=20,unique=True)
    yugam_id=models.BigAutoField(primary_key=True,unique=True)
    email_address=models.EmailField()
    gender=models.CharField(max_length=10,choices=gender_choice)
    mobile=models.BigIntegerField()
    college=models.CharField(max_length=30)
    events_name=models.ForeignKey(Event,on_delete=models.CASCADE)
    year_of_study=models.CharField(max_length=10,choices=year_option)
    

    