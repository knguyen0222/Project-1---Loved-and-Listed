from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'brand', 'category', 'size', 'color', 'condition', 'purchase_price', 'acquired_date', 'notes', 'status', 'listing_price', 'sold_price', 'platform', 'sold_date', 'image']
        widgets = {
            'acquired_date': forms.DateInput(attrs={'type': 'date'}),
            'sold_date': forms.DateInput(attrs={'type': 'date'}),
        }