from django import forms

class CheckInForm(forms.Form):
    confirmationNumber = forms.CharField(max_length=100)
    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    compliance = forms.BooleanField(required=True)
    flight_time = forms.DateTimeField()
