from unicodedata import category
from django import forms

from .models import ShoppingItem, Category


class ShoppingItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = (
            "description",
            "quantity",
            "category",
        )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            "name",
            "category_type",
        )
