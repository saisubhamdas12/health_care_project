from django import forms
from django.forms import ModelForm       
from .models import *
from django.contrib.auth.models import User
select_gender=(("Male","Male"),
               ("Female","Female"))
choice=(('Yes','Yes'),('No','No'))

Department=(('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),)
time=((' ',' '),
      ('8:30','8:30'),
      ('9:00','9:00'),
      ('9:30','9:30'),
      ('10:00','10:00'),
      ('10:30','10:30'),
      ('11:00','11:00'),
      ('11:30','11:30'),
      ('12:00','12:00'),
      ('2:00','2:00'),
      ('3:00','3:00'),
      )

data=Patient.objects.filter()
data1=Doctor.objects.filter()


      

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['Mobile','Address','Doctor_id','Department','Profile_pic','Document']
        widgets={
            'Doctor_id':forms.TextInput(attrs={'class':'form-control'}),
            'Mobile': forms.TextInput( attrs={'class': 'form-control', 'type': 'tel', 'id': 'phone-input'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'Department':forms.Select( choices=Department,attrs={'class':'form-control'}),
            'Profile_pic':forms.FileInput(attrs={'class': 'form-control-file','class':'form-control'}),
            'Document':forms.FileInput(attrs={'class': 'form-control-file','class':'form-control'}),

        }


class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = '__all__' 
        widgets={
            'Patient_id':forms.Select( choices=data,attrs={'class':'form-control'}),
            'Doctor_id':forms.Select( choices=data1,attrs={'class':'form-control'}),
            'PatientName':forms.TextInput(attrs={'class':'form-control'}),
            'DoctorName':forms.TextInput(attrs={'class':'form-control'}),
            'PatientGender': forms.Select( choices=select_gender,attrs={'class':'form-control'}),
            'DOB': forms. DateInput(attrs={'type': 'date','class':'form-control'}),
            'Phoneno': forms.TextInput( attrs={'class': 'form-control', 'type': 'tel', 'id': 'phone-input'}),
            'Emailaddress': forms.EmailInput(attrs={'class':'form-control'}),
            'Neurological': forms.Select( choices=choice,attrs={'class':'form-control'}),
            'Pychological': forms.Select( choices=choice,attrs={'class':'form-control'}),
            'Other': forms.Select( choices=choice,attrs={'class':'form-control'}),
            'Diagnosis':forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }





class PrescriptionForm(forms.ModelForm):
    class Meta:
        model=Prescriptins
        fields="__all__"  
        widgets={
            'Patient_id':forms.Select( choices=data,attrs={'class':'form-control'}),
            'Doctor_id':forms.Select( choices=data1,attrs={'class':'form-control'}),
            'Emailaddress':forms.EmailInput(attrs={'class':'form-control'}),
            'PatientGender': forms.Select( choices=select_gender,attrs={'class':'form-control'}),
            'Prescriptins':forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            
        }  
        


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#for Patient related form
class UserForm():
    class Meta:
        model=User
        fields=['username','email','password']
        widgets = { 
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}), 
        'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
        help_texts={'username':''}
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['Mobile','Address','Patient_id','Status','Profile_pic']  
        widgets={
            'Mobile':forms.TextInput( attrs={'class': 'form-control', 'type': 'tel', 'id': 'phone-input'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'Patient_id':forms.TextInput(attrs={'class':'form-control'}),
            'Profile_pic':forms.FileInput(attrs={'class': 'form-control-file','class':'form-control'}),
        }




  


class Appointmentfrom(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['Patient_id','Doctor_id','PatientName','Emailaddress','Gender','Department','Time','Patientmobile','AppointmentDate','Symptoms','Description']  
        widgets={
              
        
            'Doctor_id':forms.Select( choices=data1,attrs={'class':'form-control'}),
            'Patient_id':forms.Select( choices=data,attrs={'class':'form-control'}),
            'PatientName':forms.TextInput(attrs={'class':'form-control'}),
            
            'Emailaddress':forms.EmailInput(attrs={'class':'form-control'}),
            'Gender':forms.Select( choices=select_gender,attrs={'class':'form-control'}),
            'Department':forms.Select( choices=Department,attrs={'class':'form-control'}),
            # 'Date':forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'Time':forms.Select( choices=time,attrs={'class':'form-control'}),
            'Patientmobile':forms.TextInput( attrs={'class': 'form-control', 'type': 'tel', 'id': 'phone-input'}),
            'AppointmentDate':forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'Symptoms':forms.TextInput(attrs={'class':'form-control'}),
            'Description':forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

        



class staffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields=['Mobile','Address','Status','Profile_pic']
        widgets={
               'Mobile':forms.TextInput( attrs={'class': 'form-control', 'type': 'tel', 'id': 'phone-input'}),
               'Address':forms.TextInput(attrs={'class':'form-control'}),
               'Profile_pic':forms.FileInput(attrs={'class': 'form-control-file','class':'form-control'}), 
        }


   



        