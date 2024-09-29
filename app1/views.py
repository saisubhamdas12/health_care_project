
from django.shortcuts import render,redirect
from app1.forms import *
from app1.models import *
from app1.models import Doctor
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
# Create your views here.
def Doc_home(request):
    return render(request,'doc_contain1.html')
def Pat_home(request):
    return render(request,'pat_contain2.html')
def Staff_home(request):
    return render(request,'staff_contain3.html')
def hospital(request):
    return render(request,'front.html')

def now(request):
      return render(request,'new.html')

def new(request):
    return render(request,'doc_diagnosis.html')

def data(request):
     return render(request,'recorddata.html')
#doctor registration page:
def Doctor_registration(request):
    umf=UserForm()
    pmf=DoctorForm()
    d={'umf':umf,'pmf':pmf}
    
    if request.method=='POST' and request.FILES:
        umfd=UserForm(request.POST)
        pmfd=DoctorForm(request.POST,request.FILES)

        data =pmfd['Doctor_id'].value()
        # print(data)
        if umfd.is_valid() and pmfd.is_valid():
            Nud=umfd.save(commit=False)
            submittedpw=umfd.cleaned_data['password']
            Nud.set_password(submittedpw)
            Nud.save()

            Npd=pmfd.save(commit=False)
            Npd.User=Nud
            Npd.save()
            
            send_mail(
                'Registration',
                f'Your Hospital  Registration succefully completed.....! and this is your Doctor Id {data}',
                'saisubham2501@gmail.com',
                [Nud.email],
                fail_silently=False),
            return render(request,'doc_user_login.html')


    return render(request,'Doc_registration.html',d)
        




#Doctor login_id:
def Doc_user_login(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                # return HttpResponseRedirect(reverse('Doc_home'))
                return render(request, 'doc_contain1.html')
            else:
                return HttpResponse('Not active User')
    return render(request,'doc_user_login.html')

#Doctor logout
@login_required
def Doc_user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Doc_user_login'))

#diagnosis>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  # Import the Diagnosis model from your app

def add_diagnosis(request):
    if request.method == 'POST':
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('doc_display')  # Redirect to the appropriate page after a successful submission
    else:
        form = DiagnosisForm()
    return render(request, 'add_diagnosis.html', {'form': form,})


def add_Prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('doc_display1')  # Redirect to the appropriate page after a successful submission
    else:
        form = PrescriptionForm()

    return render(request, 'add_prescription.html', {'form': form})


def Doc_customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Diagnosis.objects.get(id=pk)
		return render(request, 'doc_record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('doc_display')
     

def Doc_delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it =Diagnosis.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('doc_display')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('doc_display')


def Doc_update_record(request, pk):
	if request.user.is_authenticated:
		current_record =Diagnosis.objects.get(id=pk)
		form = DiagnosisForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('doc_display')
		return render(request, 'doc_updates.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('doc_display')

def Doc_Display(request):
    if request.method=='GET':
        Patient_id=request.GET.get('Patient_id')
        print(Patient_id)
        if Patient_id:
            # Perform the search using the 'Patient_id'
            data1 = Diagnosis.objects.filter(Patient_id=Patient_id)
        else:
            # If 'Patient_id' is not provided, return all records
            data1 = Diagnosis.objects.all()
    else:
        # If it's not a GET request, return all records
        data1 = Diagnosis.objects.all()

    d = {'data1': data1}
    return render(request,'Doc_Display.html',d)






#prascription>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def Doc_Display1(request):
    if request.method=='GET':
        Patient_id=request.GET.get('Patient_id')
        print(Patient_id)
        if Patient_id:
            # Perform the search using the 'Patient_id'
            data1 = Prescriptins.objects.filter(Patient_id=Patient_id)
        else:
            # If 'Patient_id' is not provided, return all records
            data1 = Prescriptins.objects.all()
    else:
        # If it's not a GET request, return all records
        data1 = Prescriptins.objects.all()

    d = {'data1': data1}
    return render(request,'Doc_Display1.html',d)

def Doc_customer_record1(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Prescriptins.objects.get(id=pk)
		return render(request, 'doc_record1.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('doc_display1')
     







#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def Doc_delete_record1(request, pk):
	if request.user.is_authenticated:
		delete_it =Prescriptins.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('doc_display1')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('doc_display1')


def Doc_update_record1(request, pk):
	if request.user.is_authenticated:
		current_record =Prescriptins.objects.get(id=pk)
		form = PrescriptionForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('doc_display1')
		return render(request, 'doc_updates1.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('doc_display1')


def Doc_Doctor_id(request):
    l=[]
    if request.method=='POST':
        username=request.POST['username']
        doctor_id=request.POST['doctor_id']
        AUO=authenticate(username=username)
        data={'doctor_id':doctor_id}
        return HttpResponseRedirect(reverse('Doc_new', args=[data['doctor_id']]))
    return render(request,'doc_doctor_id.html')
      

@login_required
def Doctor_Appoinments(request,id):
    data = Doctor.objects.filter(Doctor_id=id)
    for i in data:
         res = i.Doctor_id
    return HttpResponseRedirect(reverse('Doc_new', args=[res]))

def Doc_new1(request):
    if request.method=='GET':
        Patient_id=request.GET.get('Patient_id')
    return HttpResponseRedirect(reverse('Doc_new', args=[Patient_id]))

def Doc_new(request,id,Patient_id):
    
        if Patient_id:
            # Perform the search using the 'Patient_id'
            data1 = Appointment.objects.filter(Patient_id=Patient_id)
        else:
            # If 'Patient_id' is not provided, return all records
            data1=Appointment.objects.filter(Doctor_id = id)
   

        d = {'data1': data1}
        return render(request,'doc_histroy.html',d)
   

def Doc_new(request,id):
    data1=Appointment.objects.filter(Doctor_id = id)
    d={'data1':data1,}
    return render(request,'doc_histroy.html',d)


def doctor_detail(request):
     return HttpResponseRedirect(reverse('Doc_id'))

def Doc_id(request):
    data1=Doctor.objects.all()
    d={'data1': data1}
    print(d)
    return render(request, 'pro_doctor detail.html', d)
def Doc_id1(request):
    data1=Doctor.objects.all()
    d={'data1': data1}
    print(d)
    return render(request, 'pro_doctor detail1.html', d)


     






# patient regetratision:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Madical_record(request):
    if request.method=='GET':
        Patient_id=request.GET.get('Patient_id')
        print(Patient_id)
        if Patient_id:
            # Perform the search using the 'Patient_id'
            data1 = Appointment.objects.filter(Patient_id=Patient_id)
        else:
            # If 'Patient_id' is not provided, return all records
            data1 = Appointment.objects.all()
    else:
        # If it's not a GET request, return all records
        data1 = Appointment.objects.all()

    d = {'data1': data1}
    return render(request,'madical_record.html',d)



def Patient_registration(request):
    pmu=UserForm()
    pmf=PatientForm()
    d={'pmu':pmu,'pmf':pmf}
    if request.method=='POST' and request.FILES:
        umfd=UserForm(request.POST)
        pmfd=PatientForm(request.POST,request.FILES)
        data =pmfd['Patient_id'].value()
        if umfd.is_valid() and pmfd.is_valid():
            Nud=umfd.save(commit=False)
            submittedpw=umfd.cleaned_data['password']   
            Nud.set_password(submittedpw)
            Nud.save()

            Npd=pmfd.save(commit=False)
            Npd.User.user=Nud
            Npd.save()

            send_mail(
                'Registration',
                f'Your Hospital  Registration succefully completed.....! and this is your Doctor Id {data}',
                'saisubham2501@gmail.com',
                [Nud.email],        
                fail_silently=False),
            return render(request,'pat_user_login.html')


    return render(request,'Pat_registration.html',d)


def Pat_user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=username
                return HttpResponseRedirect(reverse('Pat_home'))
            else:
                return HttpResponse('Not active User')
    return render(request,'pat_user_login.html')
               
# #Appointment booking>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def know(request):
#     data=User.objects.all()
#     for i in data:
#           print(i.id)
#     return HttpResponse('hloo')


from datetime import datetime

def Appoint(request):
    
    if request.method == 'POST':
        data2=Patient.objects.all()
        data = Appointment.objects.all()
        form = Appointmentfrom(request.POST)
        if form.is_valid():
            l = []
            m = []
            for i in data:
                m.append(i.AppointmentDate)
                l.append(i.Time)

            set = str(form.cleaned_data['Time'])
            set1 = str(form.cleaned_data['AppointmentDate'])
            set2=datetime.strptime(set1 + ' ' + set,"%Y-%m-%d %H:%M:%S")
            p=set2.time()
            q=set2.date()
            time_present = False
            date_present1 = False

            for time_obj in l:
                if time_obj == p:
                    time_present = True
                    break

            for time_obj1 in m:
                if time_obj1 == q:
                    date_present1 = True
                    break
            
          
            if date_present1:
                if time_present:
                    messages.success(request, 'On this Date, an appointment is already booked')
                    return HttpResponseRedirect(reverse('Appoint'))
                else:
                    form.save()
                    return HttpResponseRedirect(reverse('Pat_home'))
            elif not date_present1:
                if time_present:
                    form.save()
                    return HttpResponseRedirect(reverse('Pat_home'))
                else:
                    form.save()
                    return HttpResponseRedirect(reverse('Pat_home'))
            
    else:
        form = Appointmentfrom()

    return render(request, 'pat_Appointment.html', {'form': form})



# def Appoint(request):         
#     if request.method=='POST':
#         data=Appointment.objects.all()
#         form= (request.POST)
#         if form.is_valid():
#             l=[]
#             m=[]
#             for i in data:
#                 m.append(i.AppointmentDate)
#                 l.append(i.Time)
                
#             print(l)
#             print(m)
#             set=str(form.cleaned_data['Time'])
#             print(set)
#             set1=str(form.cleaned_data['AppointmentDate'])
#             hour=map(int,set.split(":"))
#             minute=map(int,set.split(":"))
#             year,month,day=map(int,set1.split("-"))
#             print(type(minute))
#             p=datetime.time(hour,minute)
#             n=datetime.date(year,month,day)
#             time_present=False
#             date_present1=False

#             for time_obj in l:
#                     if time_obj==p:
#                         time_present=True
#                         break
#             for time_obj1  in m:
#                     if time_obj1==n:
#                         date_present1=True
#                         break

                
#             if date_present1 :
#                 if time_present:
#                     messages.success(request, 'On this Date date Apointment is already booked')
#                     return HttpResponseRedirect(reverse('Appoint'))
#                 else:
#                     form.save() 
#                     return HttpResponseRedirect(reverse('Pat_home'))
#             elif not date_present1:
#                 if time_present:
#                         form.save() 
#                         return HttpResponseRedirect(reverse('Pat_home'))
#                 else:
#                     form.save()  
#                 return HttpResponseRedirect(reverse('Pat_home'))
#             # Save the form data to the database
#             return redirect('doc_display')  # Redirect to the appropriate page after a successful submission
#     else:
#         form = Appointmentfrom()                    
#     return render(request,'pat_Appointment.html',{'form':form})

def Display(request):
    
    if request.method=='GET':
        Patient_id=request.GET.get('Patient_id')
        print(Patient_id)
        if Patient_id:
            # Perform the search using the 'Patient_id'
            data1 = Appointment.objects.filter(Patient_id=Patient_id)
        else:
            # If 'Patient_id' is not provided, return all records
            data1 = Appointment.objects.all()
    else:
        # If it's not a GET request, return all records
        data1 = Appointment.objects.all()

    d = {'data1': data1}

    return render(request, 'Display.html', d)
        


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@login_required
def Diagnosis_display(request):
    if request.method=='GET':
        Patient_id=request.GET.get('Patient_id')
        print(Patient_id)
        if Patient_id:
            # Perform the search using the 'Patient_id'
            data1 = Diagnosis.objects.filter(Patient_id=Patient_id)
        else:
            # If 'Patient_id' is not provided, return all records
            data1 = Diagnosis.objects.all()
    else:
        # If it's not a GET request, return all records
        data1 = Diagnosis.objects.all()
    d={"data1":data1}
    return render(request,'pat_diagonsis.html',d)

@login_required
def Pat_dia_from(request,pk):   
    if request.user.is_authenticated:
		# Look Up Records
        customer_record = Diagnosis.objects.get(id=pk)
        return render(request, 'pat_dia_page.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('Display')
    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@login_required
def Prescription_display(request):
    if request.method=='GET':
        Patient_id=request.GET.get('Patient_id')
        print(Patient_id)
        if Patient_id:
            # Perform the search using the 'Patient_id'
            data1 = Prescriptins.objects.filter(Patient_id=Patient_id)
        else:
            # If 'Patient_id' is not provided, return all records
            data1 = Prescriptins.objects.all()
    else:
        # If it's not a GET request, return all records
        data1 = Prescriptins.objects.all()
    d={"data1":data1}
    return render(request,'pra_prescrtion.html',d)

@login_required
def Pat_pre_from(request,pk):   
    if request.user.is_authenticated:
		# Look Up Records
        customer_record = Prescriptins.objects.get(id=pk)
        return render(request, 'pat_pre_page.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('Display')
    


def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Appointment.objects.get(id=pk)
		return render(request, 'record_data.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('Display')
     

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Appointment.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('Display')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('Display')
     
def add_record(request):
	form =Appointmentfrom(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('Display')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('Display')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record =Appointment.objects.get(id=pk)
		form = Appointmentfrom(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('Display')
		return render(request, 'updates.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('Display')


@login_required
def Pat_user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Pat_user_login')); 


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#staff registration
def staff_registration(request):
    smu=UserForm()
    pmf=staffForm()
    d={'smu':smu,'pmf':pmf}
    if request.method=='POST' and request.FILES:
        umfd=UserForm(request.POST)
        pmfd=staffForm(request.POST,request.FILES)
        if umfd.is_valid() and pmfd.is_valid():
            Nud=umfd.save(commit=False)
            submittedpw=umfd.cleaned_data['password']
            Nud.set_password(submittedpw)
            Nud.save()

            Npd=pmfd.save(commit=False)
            Npd.user=Nud
            Npd.save()

            send_mail(
                'Registration',
                'Ur Hospital Registration succefully completed.....!',
                'saisubham2501@gmail.com',
                [Nud.email],        
                fail_silently=False),
            return render(request,'staff_user_login.html')


    return render(request,'staff_registration.html',d)


def Staff_user_login(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=username
                return HttpResponseRedirect(reverse('Staff_home'))
            else:
                return HttpResponse('Not active User')
    return render(request,'staff_user_login.html')

#staff logout
@login_required
def Staff_user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Staff_user_login'))


def staff_Display(request):
    if request.method=='GET':
        Patient_id=request.GET.get('Patient_id')
        print(Patient_id)
        if Patient_id:
            # Perform the search using the 'Patient_id'
            data1 = Appointment.objects.filter(Patient_id=Patient_id)
        else:
            # If 'Patient_id' is not provided, return all records
            data1 = Appointment.objects.all()
    else:
        data1 = Appointment.objects.all()
    d = {'data1': data1}
    return render(request,'staff_display.html',d)



def staff_customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Appointment.objects.get(id=pk)
		return render(request, 'staff_record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('staff_display')
     

def staff_delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Appointment.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('staff_display')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('staff_display')

# def staff_update_record(request, pk):
#       if request.user.is_authenticated:
#         current_record =Appointment.objects.get(id=pk)
#         form = Appointmentfrom(request.POST or None, instance=current_record)
#         date = form.cleaned_data['Date'].value()
#         time = form.cleaned_data['Time'].value()
#         print(date)       
#         if form.is_valid():
#                 form.save()
#                 send_mail(
#                 'Appointment Re-schedule',
#                 f'Your appointment date is {date} at {time}  ',
#                 'saisubham2501@gmail.com',
#                 [current_record.Emailaddress],        
#                 fail_silently=False),
#                 return redirect('staff_display')
#         return render(request, 'staff_updates.html', {'form':form})
#       else:
#             messages.success(request, "You Must Be Logged In...")
#             return redirect('staff_display')  

def staff_update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Appointment.objects.get(id=pk)
        if request.method == 'POST':
            form = Appointmentfrom(request.POST, instance=current_record)
            if form.is_valid():
                form.save()
                date = form.cleaned_data['AppointmentDate']
                time = form.cleaned_data['Time']
                send_mail(
                    'Appointment Re-schedule',
                    f'Your appointment date is {date} at {time}',
                    'saisubham2501@gmail.com',
                    [current_record.Emailaddress],
                    fail_silently=False
                )
                return redirect('staff_display')
        else:
            form = Appointmentfrom(instance=current_record)

        return render(request, 'staff_updates.html', {'form': form})
    else:
        messages.success(request, "You must be logged in...")
        return redirect('staff_display')






 
	
# import random
# def send_email_with_pin(request):
#     if request.method == 'GET':
#         Email= request.GET.get('Email')
#         print(Email)
#         if Email:
#             pin_code = random.randint(43212, 92345)
#             message = f'Your otp code is: {pin_code}' 
#             send_mail(
#                 'Appointment Re-schedule',
#                 message,
#                 'saisubham2501@gmail.com',
#                 [Email],
#                 fail_silently=False
#             )
#             return redirect('change_password',pin_code=pin_code)
#     return render (request,'forget_password.html')

# def change_password(request,msg):
#     if request.method=='POST': 
#             password=request.POST['password']
#             run=request.POST['username']
#             mun=request.POST['otpcode']
#             LUN=User.objects.filter(username=run)
#             if mun[0]==msg:
#                 if LUN:
#                     xm=LUN[0]
#                     xm.set_password(password)
#                     xm.save()
#                     return HttpResponseRedirect(reverse('Doc_user_login'))
#                 else:
#                     return HttpResponse('Username is not validate') 
 
#     return render (request,'forget_password.html')



def TimeCheck(request):
     
     data = Appointment.objects.all()
     l = []
     for i in data:
          print(i.Time)
          l.append(i.AppointmentDate)
     print(l)
     return HttpResponse("Correct")  




import random
def send_email_with_pin(request):
    if request.method == 'GET':
        Email = request.GET.get('Email')
        print(Email)
        if Email:
            pin_code = random.randint(43212, 92345)
            message = f'Your OTP code is: {pin_code}' 
            send_mail(
                'Change password otp',
                message,
                'saisubham2501@gmail.com',
                [Email],
                fail_silently=False
            )
            return redirect('change_password')
    return render(request, 'doc_email.html')

from django.contrib.auth.models import User
def change_password(request):
    if request.method=='POST': 
            password=request.POST['password']
            run=request.POST['username']
            mun=request.POST['otpcode']
            LUN=User.objects.filter(username=run)
        
            if LUN:
                xm=LUN[0]
                xm.set_password(password)
                xm.save()
                return HttpResponseRedirect(reverse('Doc_user_login'))
            else:
                return HttpResponse('Username is not validate') 
 
    return render (request,'forget_password.html')


import random
def pat_send_email_with_pin(request):
    if request.method == 'GET':
        Email = request.GET.get('Email')
        print(Email)
        if Email:
            pin_code = random.randint(43212, 92345)
            message = f'Your OTP code is: {pin_code}' 
            send_mail(
                'Change password otp',
                message,
                'saisubham2501@gmail.com',
                [Email],
                fail_silently=False
            )
            return redirect('change_password1')
    return render(request, 'pat_email.html')

def change_password1(request):
    if request.method=='POST': 
            password=request.POST['password']
            run=request.POST['username']
            mun=request.POST['otpcode']
            LUN=User.objects.filter(username=run)
        
            if LUN:
                xm=LUN[0]
                xm.set_password(password)
                xm.save()
                return HttpResponseRedirect(reverse('Pat_user_login'))
            else:
                return HttpResponse('Username is not validate') 
 
    return render (request,'pat_forget_password.html')


import random
def staff_send_email_with_pin(request):
    if request.method == 'GET':
        Email = request.GET.get('Email')
        print(Email)
        if Email:
            pin_code = random.randint(43212, 92345)
            message = f'Your OTP code is: {pin_code}' 
            send_mail(
                'Change password otp',
                message,
                'saisubham2501@gmail.com',
                [Email],
                fail_silently=False
            )
            return redirect('change_password2')
    return render(request, 'staff_email.html')

def change_password2(request):
    if request.method=='POST': 
            password=request.POST['password']
            run=request.POST['username']
            mun=request.POST['otpcode']
            LUN=User.objects.filter(username=run)
        
            if LUN:
                xm=LUN[0]
                xm.set_password(password)
                xm.save()
                return HttpResponseRedirect(reverse('Staff_user_login'))
            else:
                return HttpResponse('Username is not validate') 
 
    return render (request,'forget_password.html')


def new_part(name):
     if data:
          pass




























