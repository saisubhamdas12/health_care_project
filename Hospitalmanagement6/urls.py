"""
URL configuration for Hospitalmanagement6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Doc_home/', Doc_home,name='Doc_home'),
    path('Pat_home/', Pat_home,name='Pat_home'),
    path('Staff_home/',Staff_home,name='Staff_home'),


    
    path('',hospital,name='hospital'),
    path('new/',new,name='new'),
    path('now/',now,name='now'),
    
    path('change_password/',change_password,name='change_password'),
    path('send_email_with_pin/',send_email_with_pin,name='send_email_with_pin'),

    



 #doctor_,registration,login/logout url
    path('doc_registration/',Doctor_registration,name='Doctor_registration'),
    path('Doc_user_login/',Doc_user_login,name='Doc_user_login'),
    path('Doc_user_logout/',Doc_user_logout,name='Doc_user_logout'),
    path('Diagnosis/',add_diagnosis,name='Diagnosis'),
    path('doc_display/',Doc_Display,name='doc_display'),
    path('delete_record1/<int:pk>', Doc_delete_record, name='delete_record1'),
    # path('add_record/', add_record, name='add_record'),
    path('update_record1/<int:pk>', Doc_update_record, name='update_record1'),
    path('doc_display/<int:pk>',Doc_customer_record,name='display1'),

    path('Prescription/',add_Prescription,name='Prescription'),
    path('doc_display1/',Doc_Display1,name='doc_display1'),
    path('delete_record3/<int:pk>', Doc_delete_record1, name='delete_record3'),
    # path('add_record/', add_record, name='add_record'),
    path('update_record3/<int:pk>', Doc_update_record1, name='update_record3'),
    path('doc_display3/<int:pk>',Doc_customer_record1,name='display3'),
    path('Detail_Doctor/<str:id>',Doctor_Appoinments,name='Doctor_Appoinments'),
    path('Doc_new/<str:id>',Doc_new,name='Doc_new'),
    path('Doc_new1/',Doc_new1,name='Doc_new1'),
    path('Doc_Doctor_id/',Doc_Doctor_id,name='Doc_Doctor_id'),
   







    #Patient_,registration,login/logout url
    path('Pat_user_login/',Pat_user_login,name='Pat_user_login'),
    path('Pat_user_logout/',Pat_user_logout,name='Pat_user_logout'),
    path('Pat_registration/',Patient_registration,name='Patient_registration'),
    path('Appoint/',Appoint,name='Appoint'),
    path('display/',Display,name='Display'),
    path('Diagnosis_display/',Diagnosis_display,name='Diagnosis_display'),
    path('delete_record/<int:pk>', delete_record, name='delete_record'),
    # path('add_record/', add_record, name='add_record'),
    path('update_record/<int:pk>', update_record, name='update_record'),
    path('display/<int:pk>',customer_record,name='display'),
    path('pat_dia_page/<int:pk>',Pat_dia_from,name='pat_dia_page'),
    path('pat_pre_page/<int:pk>',Pat_pre_from,name='pat_pre_page'),
    path('Prescription_display/',Prescription_display,name='Prescription_display'),
    path('pat_send_email_with_pin/',pat_send_email_with_pin,name='pat_send_email_with_pin'),
    path('change_password1/',change_password1,name='change_password1'),

   
   
   

    path('Madical_record/',Madical_record,name='Madical_record'),
    path('doctor_detail/',doctor_detail,name='doctor_detail'),
    path('Cardiologist/',Doc_id,name='Doc_id'),
    path('Dermatologists/',Doc_id1,name='Doc_id1'),



    #staff_,registration,login/logout url
    path('staff_registration/',staff_registration,name='staff_registration'),
    path('Staff_user_login/',Staff_user_login,name='Staff_user_login'),
    path('Staff_user_logout/',Staff_user_logout,name='Staff_user_logout'),
    path('staff_display/',staff_Display,name='staff_display'),
    path('delete_record2/<int:pk>', staff_delete_record, name='delete_record2'),
    # path('add_record/', add_record, name='add_record'),
    path('update_record2/<int:pk>', staff_update_record, name='update_record2'),
    path('staff_display/<int:pk>',staff_customer_record,name='display2'),
    path('staff_send_email_with_pin',staff_send_email_with_pin,name='staff_send_email_with_pin'),
    path('change_password2/',change_password2,name='change_password2'),
    path('checkTime/',TimeCheck),
    


    
]




