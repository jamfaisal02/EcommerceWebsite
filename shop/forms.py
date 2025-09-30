
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Product name'}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'rows': 4, 'placeholder': 'Description'}),
            'price': forms.NumberInput(attrs={'class': 'input', 'step': '0.01', 'placeholder': 'Price'}),
        }
