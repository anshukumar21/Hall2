from django import forms
import datetime

#Admin has to enter the announcement maintext. Other details are handled internally
class AnnouncementForm(forms.Form):
    announcement = forms.CharField(required=True)

#Admin has to enter the event headline, event date, event time(optional). Other details are handled internally
class EventForm(forms.Form):
    event_headline = forms.CharField(required=True)
    event_date = forms.DateField(required=True)
    event_time = forms.TimeField()