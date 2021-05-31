from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
     

        
# class SignUpForm(forms.ModelForm):
#         username = forms.CharField(max_length=30, required=False, help_text='Optional.')
#         email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#        
#         class Meta:
#                 model = User
#                 fields = ['username','password','email']
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2', 
            ]
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=False)
    email = forms.EmailInput()
    password = forms.CharField(widget=forms.PasswordInput)
    
