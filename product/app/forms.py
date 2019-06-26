from django import forms
from app.models import catogery,product

class catogeryForms(forms.ModelForm):
    model=catogery
    fields="pid","p_product","p_price",

class productForms(forms.ModelForm):
    model=product
    fields="l_id","l_product","l_name","l_price",