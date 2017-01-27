from django.test import TestCase
from beutifulhome.forms import (
    ContactForm, NO_EMAIL_ADDRESS_MESSAGE, INVALID_EMAIL_ADDRESS_MESSAGE,
    NO_NAME_MESSAGE, NO_SUBJECT_MESSAGE, NO_TYPE_MESSAGE, NO_CONTENT_MESSAGE)


class ContactFormTest(TestCase):

    def test_form_renders_return_email_input(self):
        form = ContactForm()
        self.assertIn('placeholder="Your email address"', form.as_p())

    def test_form_renders_contact_name_input(self):
        form = ContactForm()
        self.assertIn('placeholder="Your name"', form.as_p())

    def test_form_renders_message_subject_input(self):
        form = ContactForm()
        self.assertIn('placeholder="Message subject"', form.as_p())

    def test_form_renders_message_type_input(self):
        form = ContactForm()
        self.assertIn('name="message_type"', form.as_p())

    def test_form_renders_message_content_input(self):
        form = ContactForm()
        self.assertIn('placeholder="Your message"', form.as_p())

    def test_form_renders_submit_button(self):
        form = ContactForm()
        self.assertIn('value="Send"', form.as_p())

    def test_form_validation_for_missing_email(self):
        form = ContactForm(data={
            'return_email': '', 'contact_name': 'Philip Jones',
            'message_subject': 'Hello', 'message_type': 'Query',
            'message_content': 'Hello message'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['return_email'],
            [NO_EMAIL_ADDRESS_MESSAGE])

    def test_form_validation_for_non_valid_email_address(self):
        form = ContactForm(data={
            'return_email': 'invalidemailstring',
            'contact_name': 'Philip Jones', 'message_subject': 'Hello',
            'message_type': 'Query', 'message_content': 'Hello message'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['return_email'], [INVALID_EMAIL_ADDRESS_MESSAGE])

    def test_form_validation_for_missing_name(self):
        form = ContactForm(data={
            'return_email': 'noone@example.com', 'contact_name': '',
            'message_subject': 'Hello', 'message_type': 'Query',
            'message_content': 'Hello message'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['contact_name'], [NO_NAME_MESSAGE])

    def test_form_validation_for_missing_subject(self):
        form = ContactForm(data={
            'return_email': 'noone@example.com',
            'contact_name': 'Philip Jones', 'message_subject': '',
            'message_type': 'Query', 'message_content': 'Hello message'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['contact_name'], [NO_SUBJECT_MESSAGE])

    def test_form_validation_for_missing_message_type(self):
        form = ContactForm(data={
            'return_email': 'noone@example.com',
            'contact_name': 'Philip Jones', 'message_subject': 'Hello',
            'message_type': '', 'message_content': 'Hello message'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['contact_name'], [NO_TYPE_MESSAGE])

    def test_form_validation_for_missing_content(self):
        form = ContactForm(data={
            'return_email': 'noone@example.com',
            'contact_name': 'Philip Jones', 'message_subject': 'Hello',
            'message_type': 'Query', 'message_content': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['contact_name'], [NO_CONTENT_MESSAGE])
