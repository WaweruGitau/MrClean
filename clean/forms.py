# clean/forms.py
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'item', 'quantity', 'delivery_date']

        widgets = {
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'item': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'delivery_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
