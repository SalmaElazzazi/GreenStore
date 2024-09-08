from django import forms
from .models import Contact 

class Contact_Us(forms.ModelForm): 
    class Meta:
        model = Contact
        fields = ('name','email', 'message')  
