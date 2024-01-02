from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


# - Register/Create a user
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# - Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a complaint/User
class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']


# - Update a cpmplaint/User
class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']


# - report a suspect/User
class reportSuspectForm(forms.ModelForm):

    class Meta:
        model = ReportSuspect
        fields = '__all__'
        widgets = {
            'sex': forms.Select(attrs={'class': 'form-control'}),
        }


# - fill in a crime report/Admin
#class CrimeReportForm(forms.ModelForm):
#    class Meta:
#        model = CrimeReport
#        fields = ['title', 'suspect_name', 'description', 'status']
