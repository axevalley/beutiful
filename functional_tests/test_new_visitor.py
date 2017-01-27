from . base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def check_page_header(self, url, text):
        self.browser.get(self.server_url + url)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn(text.lower(), header_text.lower())

    def test_title_tag(self):
        self.browser.get(self.server_url)
        self.assertIn('BE-U-tiful', self.browser.title)

    def test_index(self):
        self.check_page_header('/', 'Beutiful')

    def test_about(self):
        self.check_page_header('/about/', 'About')

    def test_products(self):
        self.check_page_header('/products/', 'Products')

    def test_services(self):
        self.check_page_header('/services/', 'Services')

    def test_friends(self):
        self.check_page_header('/friends/', 'Friends')

    def test_contact(self):
        self.check_page_header('/contact', 'Contact')
