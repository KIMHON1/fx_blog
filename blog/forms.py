from django import forms
from .models import ContactFormMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        
