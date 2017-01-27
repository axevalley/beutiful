from django.test import TestCase
from beutifulhome.forms import ContactForm


class HomePageTest(TestCase):

    def test_uses_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'beutifulhome/index.html')


class AboutPageTestTest(TestCase):

    def test_uses_about_template(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'beutifulhome/about.html')


class ContactPageTest(TestCase):

    def test_uses_contact_template(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'beutifulhome/contact.html')

    def test_displays_contact_form(self):
        response = self.client.get('/contact/')
        self.assertIsInstance(response.context['form'], ContactForm)
        self.assertContains(response, 'name="return_email"')
        self.assertContains(response, 'name="contact_name"')
        self.assertContains(response, 'name="message_subject"')
        self.assertContains(response, 'name="message_type"')
        self.assertContains(response, 'name="message_content"')


class FriendsPageTest(TestCase):

    def test_uses_friends_template(self):
        response = self.client.get('/friends/')
        self.assertTemplateUsed(response, 'beutifulhome/friends.html')


class ProductsPageTest(TestCase):

    def test_uses_products_template(self):
        response = self.client.get('/products/')
        self.assertTemplateUsed(response, 'beutifulhome/products.html')


class ServicesPageTest(TestCase):

    def test_uses_services_template(self):
        response = self.client.get('/services/')
        self.assertTemplateUsed(response, 'beutifulhome/services.html')
