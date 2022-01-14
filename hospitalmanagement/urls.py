
from django.contrib import admin
from django.urls import path
from hospital import views
from django.contrib.auth.views import LoginView,LogoutView


#-------------FOR ADMIN RELATED URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),


    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),


    path('adminclick', views.adminclick_view),
    path('doctorclick', views.doctorclick_view),
    path('receptionistclick', views.receptionistclick_view),

    path('adminsignup', views.admin_signup_view),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('patientsignup', views.patient_signup_view),
    
    path('adminlogin', LoginView.as_view(template_name='hospital/adminlogin.html')),
    path('doctorlogin', LoginView.as_view(template_name='hospital/doctorlogin.html')),
    path('patientlogin', LoginView.as_view(template_name='hospital/patientlogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view,name='admin-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admin-add-doctor', views.admin_add_doctor_view,name='admin-add-doctor'),
    path('admin-approve-doctor', views.admin_approve_doctor_view,name='admin-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('admin-view-doctor-specialisation',views.admin_view_doctor_specialisation_view,name='admin-view-doctor-specialisation'),


    path('admin-patient', views.admin_patient_view,name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view,name='admin-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('admin-add-patient', views.admin_add_patient_view,name='admin-add-patient'),
    path('admin-approve-patient', views.admin_approve_patient_view,name='admin-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('admin-discharge-patient', views.admin_discharge_patient_view,name='admin-discharge-patient'),
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
    path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),


    path('admin-appointment', views.admin_appointment_view,name='admin-appointment'),
    path('admin-view-appointment', views.admin_view_appointment_view,name='admin-view-appointment'),
    path('admin-add-appointment', views.admin_add_appointment_view,name='admin-add-appointment'),
    
]


#---------FOR DOCTOR RELATED URLS-------------------------------------
urlpatterns +=[
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),

    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),

    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),
]





#---------FOR RECEPTIONIST RELATED URLS-------------------------------------
urlpatterns +=[

    path('receptionistsignup', views.receptionist_signup_view),
    path('receptionist-dashboard', views.receptionist_dashboard_view,name='receptionist-dashboard'),
    path('admin-receptionist', views.admin_receptionist_view,name='admin-receptionist'),
    path('receptionistlogin', LoginView.as_view(template_name='hospital/receptionistlogin.html')),

    path('approve-receptionist/<int:pk>', views.approve_receptionist_view,name='approve-receptionist'),
    path('reject-receptionist/<int:pk>', views.reject_receptionist_view,name='reject-receptionist'),
    path('delete-receptionist/<int:pk>', views.delete_receptionist_view,name='delete-receptionist'),
    path('receptionist-change-hospital', views.receptionist_change_hospital_view,name='receptionist-change-hospital'),
    path('receptionist-patient', views.receptionist_patient_view,name='receptionist-patient'),
    path('receptionist-view-patient', views.receptionist_view_patient_view,name='receptionist-view-patient'),
    path('receptionist-add-patient', views.receptionist_add_patient_view,name='receptionist-add-patient'),



    path('receptionist-appointment', views.receptionist_appointment_view,name='receptionist-appointment'),
    path('receptionist-view-appointment', views.receptionist_view_appointment_view,name='receptionist-view-appointment'),
    path('receptionist-add-appointment', views.receptionist_add_appointment_view,name='receptionist-add-appointment'),
]
#---------FOR HOSPITAL RELATED URLS-------------------------------------
urlpatterns +=[

    path('hospitalclick', views.hospitalclick_view,name='hospitalclick'),
    path('hospitalsignup', views.hospitalsignup_view,name='hospitalsignup'),
    path('hospitallogin', LoginView.as_view(template_name='hospital/hospitallogin.html')),
    path('hospital-dashboard', views.hospital_dashboard_view,name='hospital-dashboard'),
    path('change-hospital', views.change_hospital_view,name='change-hospital'),

    
    path('hospital-change-history', views.hospital_change_history_view,name='hospital-change-history'),
    path('admin-hospital-change', views.admin_hospital_change_view,name='admin-hospital-change'),

    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    path('reject-request/<int:pk>', views.disapprove_request_view,name='reject-request'),

    path('hospital-doctor', views.hospital_doctor_view,name='hospital-doctor'),
    path('hospital-patient', views.hospital_patient_view,name='hospital-patient'),



]
#---------FOR MINISTRY RELATED URLS-------------------------------------
urlpatterns +=[

    path('ministryclick', views.ministryclick_view,name='ministryclick'),
    path('ministrysignup', views.ministrysignup_view,name='ministrysignup'),
    path('ministrylogin', LoginView.as_view(template_name='hospital/ministrylogin.html')),
    path('ministry-dashboard', views.ministry_dashboard_view,name='ministry-dashboard'),
    path('ministry-hospital', views.ministry_hospital_view,name='ministry-hospital'),

    path('approve-hospital/<int:pk>', views.approve_hospital_view,name='approve-hospital'),
    path('reject-hospital/<int:pk>', views.reject_hospital_view,name='reject-hospital'),
    path('delete-hospital/<int:pk>', views.delete_hospital_view,name='delete-hospital'),

    path('ministry-doctor', views.ministry_doctor_view,name='ministry-doctor'),
    path('ministry-patient', views.ministry_patient_view,name='ministry-patient'),
    
    



]

