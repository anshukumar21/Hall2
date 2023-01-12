from django import forms

#Extra ordering form (For now item can only be added one at a time)
class OrderForm(forms.Form):
    id = forms.IntegerField(required=True)
    option = forms.BooleanField(required=False, initial=False)