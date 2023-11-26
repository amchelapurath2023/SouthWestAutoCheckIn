from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class CheckInForm(forms.Form):
    confirmationNumber = forms.CharField(max_length=100)
    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    compliance = forms.BooleanField(required=True)
    flight_time = forms.DateTimeField()
    phoneNumber = forms.CharField(max_length=15)
