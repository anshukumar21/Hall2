from django import forms

class AnnouncementForm(forms.Form):
    announcement = forms.CharField(required=True)

class EventForm(forms.Form):
    event_headline = forms.CharField(required=True)
    event_date = forms.DateField(required=True)
    event_time = forms.TimeField()