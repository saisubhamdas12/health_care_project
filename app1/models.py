from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import uuid
User=get_user_model()
# Create your models here.

departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),

]
class User(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=100)
    def __str__(self):
        return self.user.text
    
def generate_short_uuid():
    return str(uuid.uuid4())[:5]



Gender=[('Male','Male'),('Famale','Famale')]
class Doctor(models.Model):
    Doctor_id=models.CharField(max_length=5,primary_key=True, default=generate_short_uuid)
    username=models.CharField(max_length=100)
    Gender=models.CharField(max_length=50,choices=Gender,default='Male')
    Profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    Address = models.CharField(max_length=40)
    Mobile = models.CharField(max_length=20,null=True)
    Department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    Status=models.BooleanField(default=True)
    Document=models.FileField()	
   
    def __str__(self):
        return self.Doctor_id


#patient registration
class Patient(models.Model):
    Patient_id=models.CharField(max_length=6,primary_key=True, default=generate_short_uuid)
    username=models.CharField(max_length=100)
    Gender=models.CharField(max_length=50,choices=Gender,default='Male')
    Profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    Address = models.CharField(max_length=40)
    Mobile = models.CharField(max_length=20,null=True)
    Status=models.BooleanField(default=True)
    def __str__(self):
        return self.Patient_id


#staff registraion
class Staff(models.Model):
    Profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    Gender=models.CharField(max_length=50,choices=Gender,default='Male')
    Address = models.CharField(max_length=40)
    Mobile = models.CharField(max_length=20,null=True)
    Status=models.BooleanField(default=True)


#Appointment    
class Appointment(models.Model):
    Patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Doctor_id= models.ForeignKey(Doctor,on_delete=models.CASCADE)
    PatientName=models.CharField(max_length=40,null=True)
    Emailaddress=models.EmailField()
    Gender=models.CharField(max_length=100)
    Department= models.CharField(max_length=100)
    Date=models.DateField(auto_now=True)
    Time=models.TimeField()
    Patientmobile = models.CharField(max_length=20,null=True)
    AppointmentDate=models.DateField()
    Symptoms = models.CharField(max_length=100,null=True)
    Description=models.TextField(max_length=500)
    

class Booking(models.Model):
    Patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Doctor_id= models.ForeignKey(Doctor,on_delete=models.CASCADE)
    PatientName=models.CharField(max_length=40,null=True)
    DoctorName=models.CharField(max_length=40,null=True)
    Emailaddress=models.EmailField()
    Gender=models.CharField(max_length=100)
    Department= models.CharField(max_length=100)
    Date=models.DateField()
    Time=models.TimeField()
    Patientmobile = models.CharField(max_length=20,null=True)
    AppointmentDate=models.DateField(auto_now=True)
    Symptoms = models.CharField(max_length=100,null=True)
    Description=models.TextField(max_length=500)
    
    
#Diagnosis
class Diagnosis(models.Model):
    Patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Doctor_id= models.ForeignKey(Doctor,on_delete=models.CASCADE)
    PatientName=models.CharField(max_length=40,null=True)
    DoctorName=models.CharField(max_length=40,null=True)
    PatientGender=models.CharField(max_length=100)
    DOB=models.DateField()
    Phoneno=models.CharField(max_length=10)
    Emailaddress=models.EmailField()
    Neurological=models.CharField(max_length=100,default='no')
    Pychological=models.CharField(max_length=100,default='no')
    Other=models.CharField(max_length=100,default='no')
    Diagnosis=models.TextField()


class Prescriptins(models.Model):
    Patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Doctor_id= models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Emailaddress=models.EmailField()
    PatientGender=models.CharField(max_length=50)
    Prescriptins=models.TextField()




# Create your models here.


