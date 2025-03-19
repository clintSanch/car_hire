from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Booking

# User Registration Form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Booking Form
from django import forms
from .models import Booking
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pickup_date', 'return_date', 'customer_name', 'contact']

        widgets = {
            'pickup_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': date.today().isoformat()}),
            'return_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
        }

    def clean_pickup_date(self):
        """Ensure the pickup date is today or later."""
        pickup_date = self.cleaned_data['pickup_date']
        if pickup_date < date.today():
            raise forms.ValidationError("Pickup date cannot be in the past.")
        return pickup_date

    def clean_return_date(self):
        """Ensure the return date is after the pickup date."""
        pickup_date = self.cleaned_data.get('pickup_date')
        return_date = self.cleaned_data['return_date']

        if pickup_date and return_date <= pickup_date:
            raise forms.ValidationError("Return date must be after the pickup date.")
        return return_date

    def clean_customer_name(self):
        """Ensure customer name is at least 3 characters long."""
        name = self.cleaned_data['customer_name']
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    def clean_contact(self):
        """Ensure contact is a valid phone number (simple regex validation)."""
        contact = self.cleaned_data['contact']
        if not contact.isdigit() or len(contact) < 10:
            raise forms.ValidationError("Enter a valid phone number (at least 10 digits).")
        return contact
