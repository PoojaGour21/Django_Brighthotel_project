from django import forms
from hotelapp.models import Register, Contact, Conventionhall,Rating,Booking,Notifications


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"


class ConventionhallForm(forms.ModelForm):
    class Meta:
        model = Conventionhall
        fields = "__all__"
class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields = "__all__"

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=["email", "required_date", "from_time", "to_time", "no_of_guests","conventionhall1","cost"]

class NotificationsForm(forms.ModelForm):
    class Meta:
        model=Notifications
        fields="__all__"