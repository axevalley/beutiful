import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    def setUp(self):
        self.browser = self.get_browser()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def get_browser(self):
        return webdriver.Firefox(firefox_binary=FirefoxBinary(
            firefox_path='C:\\Program Files\\Mozilla FirefoxESR\\firefox.exe'))

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
