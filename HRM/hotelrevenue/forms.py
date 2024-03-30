# forms.py

from django import forms
from .models import Booking, Guest

class BookingForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    check_in_date = forms.DateField()
    check_out_date = forms.DateField()

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'email', 'phone_number']
