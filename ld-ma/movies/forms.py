from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
        
        
class SignUpForm(forms.ModelForm):
        username = forms.CharField(max_length=30, required=False, help_text='Optional.')
        email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
       
        class Meta:
                Model = User
                fields = ['username','password','password1','email']
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=False)
    email = forms.EmailInput()
    password = forms.CharField(widget=forms.PasswordInput)
    
