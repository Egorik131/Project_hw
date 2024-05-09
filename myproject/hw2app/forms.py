import datetime
from django import forms
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    price = forms.DecimalField(min_value=0, max_digits=8, decimal_places=2)
    quantity = forms.IntegerField(min_value=0)
    date_in = forms.DateField(initial=datetime.date.today)
    img_file = forms.ImageField()


