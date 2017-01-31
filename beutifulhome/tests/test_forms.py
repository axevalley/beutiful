from django.test import TestCase
from beutifulhome.forms import (
    ContactForm, NO_EMAIL_ADDRESS_MESSAGE, INVALID_EMAIL_ADDRESS_MESSAGE,
    NO_NAME_MESSAGE, NO_SUBJECT_MESSAGE, NO_CONTENT_MESSAGE,
    INVALID_PHONE_MESSAGE)


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

    def test_form_renders_contact_phone_input(self):
        form = ContactForm()
        self.assertIn('name="contact_phone"', form.as_p())

    def test_form_renders_message_content_input(self):
        form = ContactForm()
        self.assertIn('placeholder="Your message"', form.as_p())

    def test_form_validation_for_missing_email(self):
        form = ContactForm(data={
            'return_email': '', 'contact_name': 'Philip Jones',
            'message_subject': 'Hello', 'contact_phone': '09879 46587',
            'message_content': 'Hello message'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['return_email'],
            [NO_EMAIL_ADDRESS_MESSAGE])

    def test_form_validation_for_non_valid_email_address(self):
        form = ContactForm(data={
            'return_email': 'invalidemailstring',
            'contact_name': 'Philip Jones', 'message_subject': 'Hello',
            'contact_phone': '09879 46587', 'message_content': 'Hello message'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['return_email'], [INVALID_EMAIL_ADDRESS_MESSAGE])

    def test_form_validation_for_missing_name(self):
        form = ContactForm(data={
            'return_email': 'noone@example.com', 'contact_name': '',
            'message_subject': 'Hello', 'contact_phone': 'Query',
            'message_content': 'Hello message'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['contact_name'], [NO_NAME_MESSAGE])

    def test_form_validation_for_missing_subject(self):
        form = ContactForm(data={
            'return_email': 'noone@example.com',
            'contact_name': 'Philip Jones', 'message_subject': '',
            'contact_phone': '09879 46587',
            'message_content': 'Hello message'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['message_subject'], [NO_SUBJECT_MESSAGE])

    def test_form_can_be_processed_without_phone_supplied(self):
        form = ContactForm(data={
            'return_email': 'noone@example.com',
            'contact_name': 'Philip Jones', 'message_subject': 'Hello',
            'contact_phone': '', 'message_content': 'Hello message'})
        self.assertTrue(form.is_valid())

    def test_only_number_can_be_submitted_in_phone_field(self):
        form = ContactForm(data={
            'return_email': 'noone@example.com',
            'contact_name': 'Philip Jones', 'message_subject': '',
            'contact_phone': 'Hello Text',
            'message_content': 'Hello message'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['contact_phone'], [INVALID_PHONE_MESSAGE])

    def test_form_validation_for_missing_content(self):
        form = ContactForm(data={
            'return_email': 'noone@example.com',
            'contact_name': 'Philip Jones', 'message_subject': 'Hello',
            'contact_phone': '09879 46587', 'message_content': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['message_content'], [NO_CONTENT_MESSAGE])
