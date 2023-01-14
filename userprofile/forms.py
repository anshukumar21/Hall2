from django import forms

class MailForm(forms.Form):
    subject = forms.CharField(required=True)
    body = forms.CharField(required=True)