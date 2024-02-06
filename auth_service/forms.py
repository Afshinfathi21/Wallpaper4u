from django import forms
from .models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm,TextInput,ChoiceField,Textarea

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
                'class': "form-control", 
                'placeholder': 'Password'
                }))
    password2 = forms.CharField(
        label="Confirmation Password", widget=forms.PasswordInput(
            attrs={
                'class': "form-control", 
                'placeholder': 'Confirmation Password'
                }
        )
    )
    username=forms.CharField(label='Username',widget=TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Username'
                }))
    class Meta:
        
        model = CustomUser
        fields = ["username",'email','password1','password2','bio','profile_img']
        widgets = {
            'email': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Email'
                }),
            
            }

    def clean_username(self):
        username=self.cleaned_data.get("username")
        user_name=CustomUser.objects.filter(username=username)
        if user_name.exists():
            raise ValidationError('Username Taken.')
        else:
            return username
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        return password2

    
    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserloginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}),
        label="Username")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
