from django import forms

class OrderForm(forms.Form):
    id = forms.IntegerField(required=True)
    quantity = forms.IntegerField(initial=1)
    option = forms.BooleanField(required=False, initial=False)