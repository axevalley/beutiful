from django import forms
import re


NO_EMAIL_ADDRESS_MESSAGE = "Please supply a return email address"
INVALID_EMAIL_ADDRESS_MESSAGE = "Please provide a valid email address"
NO_NAME_MESSAGE = "Please enter your name"
NO_SUBJECT_MESSAGE = "Please provide a subject for your message"
INVALID_PHONE_MESSAGE = "Please provide a valid phone number or leave blank"
NO_CONTENT_MESSAGE = "Please provide a message"


class ContactForm(forms.Form):
    return_email = forms.EmailField(
        required=True, error_messages={
            'required': NO_EMAIL_ADDRESS_MESSAGE,
            'invalid': INVALID_EMAIL_ADDRESS_MESSAGE},
        widget=forms.fields.EmailInput(
            attrs={
                'placeholder': 'Your email address',
                'class': 'contact_form_input'}))

    contact_name = forms.CharField(
        required=True, error_messages={'required': NO_NAME_MESSAGE},
        widget=forms.fields.TextInput(attrs={
            'placeholder': 'Your name',
            'class': 'contact_form_input'}))

    message_subject = forms.CharField(
        required=True, error_messages={'required': NO_SUBJECT_MESSAGE},
        widget=forms.fields.TextInput(attrs={
            'placeholder': 'Message subject',
            'class': 'contact_form_input'}))

    contact_phone = forms.CharField(
        required=False, widget=forms.fields.TextInput(attrs={
            'placeholder': 'Your phone number (optional)',
            'class': 'contact_form_input'}))

    message_content = forms.CharField(
        required=True, error_messages={'required': NO_CONTENT_MESSAGE},
        widget=forms.Textarea(attrs={
            'placeholder': 'Your message',
            'class': 'contact_form_input'}))

    def clean_contact_phone(self):
        phone_regex = re.compile('^\+?1?\d{9,15}$')
        number = self.cleaned_data['contact_phone']
        if len(number) > 0 and phone_regex.match(number) is None:
            raise forms.ValidationError(INVALID_PHONE_MESSAGE, code='invalid')
        return self.cleaned_data
