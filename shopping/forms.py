from django import forms
from .models import Order

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    
from django import forms
from .models import Order  # Ensure you import your Order model

class CheckoutForm(forms.ModelForm):
    email = forms.EmailField(label="Email address")
    city = forms.CharField(label="Town / City")
    address = forms.CharField(label="Street address")  # Fixed typo from 'adress' to 'address'
    postal_code = forms.CharField(label="ZIP Code")
    notes = forms.CharField(label="Additional information", widget=forms.Textarea)

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'phone', 'email', 'address', 'city', 'postal_code', 'notes', 'paid')
