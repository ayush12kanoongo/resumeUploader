from django.db import models

STATE_CHOICE=(
    ('maharashtra','Maharashtra'),
    ('goa','GOA'),
    ('pune','PUNE'),
    ('mumbai','MUMBAI'),
    

)
# Create your models here.
class Resume(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False ,auto_now_add=False)
    gender=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE, max_length=50)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='profileimg', blank=False)
    my_file=models.FileField(upload_to='doc' , blank=False)

    