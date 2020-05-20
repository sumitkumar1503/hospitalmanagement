from django import forms
from django.contrib.auth.models import User
from . import models



#for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']


#for student related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department','status']



#for teacher related form
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Patient
        fields=['address','mobile','status','symptoms']





#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
