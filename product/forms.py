from django import forms

from product.models import (
    Category,
    User,
    Supplier,
    ProductReview,
    ProductImage,
    Product,
    PriceHistory
)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'category',
            'stock',
        ]
        
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'color: red',
                    }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                    }
            ),
        }