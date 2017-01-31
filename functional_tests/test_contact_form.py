from . base import FunctionalTest


class TestContactForm(FunctionalTest):

    def get_input_box(self, id_):
        return self.browser.find_element_by_id(id_)

    def get_email_input_box(self):
        return self.get_input_box('return_email')

    def get_name_input_box(self):
        return self.get_input_box('contact_name')

    def get_subject_input_box(self):
        return self.get_input_box('message_subject')

    def get_phone_input_box(self):
        return self.get_input_box('contact_phone')

    def get_content_input_box(self):
        return self.get_input_box('message_content')

    def get_submit_button(self):
        return self.get_input_box('send_button')

    def test_can_submit_valid_contact_form(self):
        # Edith visits the contact page and tries to submit a query.
        self.browser.get(self.server_url)
        self.get_email_input_box().send_keys('someone@example.com')
        self.get_name_input_box().send_keys('Someone Somewhere')
        self.get_subject_input_box().send_keys('Greetings')
        self.get_type_input_box().send_keys('Query')
        self.get_content_input_box().send_keys(
            'Hello,\n I am interested in your products.\n\n\tYours,'
            ' Someone Somewhere')
        self.get_submit_button(self).click()

    def test_enter_does_not_submit_form(self):
        self.fail('Write the test')

    def test_invalid_input(self):
        self.fail('Write the test')
