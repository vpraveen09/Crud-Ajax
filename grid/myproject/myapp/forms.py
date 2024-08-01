from django import forms
from .models import Student

class LoginForm(forms.Form):
       username = forms.CharField(max_length=100)
       password = forms.CharField(widget=forms.PasswordInput)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailid', 'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'passwordid', 'placeholder': 'Enter your password'}),
        }
        error_messages = {
            'name': {
                'required': 'Please enter name.',
            },
            'email': {
                'required': 'Please enter email.',
            },
            'password': {
                'required': 'Please enter password.',
            }
        }
