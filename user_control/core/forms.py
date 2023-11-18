from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            
        ]
        widgets = {
            'username'  : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name'  : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name'  : forms.TextInput(attrs={'class': 'form-control'}),
            'email'  : forms.EmailInput(attrs={'class': 'form-control'}),
            'password'  : forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_superuser',
            'is_active',
            'is_staff' ,
            
        ]
        widgets = {
            'username'  : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name'  : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name'  : forms.TextInput(attrs={'class': 'form-control'}),
            'email'  : forms.EmailInput(attrs={'class': 'form-control'}),
            'is_superuser'  : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active'  : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff'  : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
