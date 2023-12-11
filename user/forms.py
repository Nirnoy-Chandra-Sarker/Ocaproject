from .models import User, Student, StudentProfile
from django import forms


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone_number', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class StudentRegisterForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['photo', 'name', 'email', 'phone_number', 'password']
        labels = {
            'name': '',
            'phone_number': '',
            'email': '',
            'password': '',
        }

        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Your Photo'}),
            'name': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control my-3',  'placeholder': 'Enter Your Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Enter Your Phone Number'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control my-3',  'placeholder': 'Enter Your Password'})
        }

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['std_id', 'department', 'semester', 'add_year']
        widgets = {
            'std_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Student ID'}),
            'add_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Addmission Year'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
        }