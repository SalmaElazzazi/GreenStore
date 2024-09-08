from django.contrib.auth.models import User 
from django import forms

class UserCreationForm(forms.ModelForm):
    
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="verification password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name","password1","password1")
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('The password does not match')
        return cd['password2']
    
    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('A user with this name already exists.')
        return cd['username']
    
class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("username","password")
    