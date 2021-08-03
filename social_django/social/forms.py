from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Post, Profile

class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': '¿Que que tienes que decir?'}), required=True)   
    class Meta:
        model = Post
        fields = ['content']
           
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]
        help_texts = {k:"" for k in fields}

class ProfileForm(forms.ModelForm):
    image = forms.ImageField(label=(''),required=False, error_messages = {'invalid':("Solo imagenes")}, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = [
            'bio',
            'image',
             
        ]
                    
class PasswordCha(PasswordChangeForm): 
    old_password =forms.CharField(label='Contraseña actual', widget=forms.PasswordInput(attrs={'class': 'form-control',  'type':'password'}))
    new_password1 = forms.CharField( label='Contraseña', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(label='Confirmar Contraseña', max_length=100,widget=forms.PasswordInput (attrs={'class': 'form-control', 'type':'password'}))
    
    class Meta:
        model = User
        fields=('old_password', 'new_password1', 'new_password2')
        
       
           
 
              