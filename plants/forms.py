from django import forms
from .models import Review 

class NewReviewForm(forms.ModelForm): 
    class Meta:
        model = Review
        fields = ('name','email','rating', 'comment')  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)], attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
