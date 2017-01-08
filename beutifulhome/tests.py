from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'beutifulhome/index.html')

    def test_uses_about_template(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'beutifulhome/about.html')

    def test_uses_contact_template(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'beutifulhome/contact.html')

    def test_uses_friends_template(self):
        response = self.client.get('/friends/')
        self.assertTemplateUsed(response, 'beutifulhome/friends.html')

    def test_uses_products_template(self):
        response = self.client.get('/products/')
        self.assertTemplateUsed(response, 'beutifulhome/products.html')

    def test_uses_services_template(self):
        response = self.client.get('/services/')
        self.assertTemplateUsed(response, 'beutifulhome/services.html')
