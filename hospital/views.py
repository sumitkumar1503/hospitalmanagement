from django.shortcuts import render
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test




def test(request):
    return render(request,'hospital/admin_base.html')


# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/index.html')

def admin_dashboard_view(request):
    return render(request,'hospital/admin_dashboard.html')

def admin_doctor_view(request):
    return render(request,'hospital/admin_doctor.html')


def admin_patient_view(request):
    return render(request,'hospital/admin_patient.html')

def admin_appointment_view(request):
    return render(request,'hospital/admin_appointment.html')









# for aboutus and contact ussssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss (by sumit)
def aboutus_view(request):
    return render(request,'hospital/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message, EMAIL_HOST_USER, ['wapka1503@gmail.com'], fail_silently = False)
            return render(request, 'hospital/contactussuccess.html')
    return render(request, 'hospital/contactus.html', {'form':sub})
