from django import forms
from .models import *




class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['item_name', 'price', 'photo', 'category']

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
       
        
