from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import unittest, time, os, sys


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            # print(" , ", arg)
            if '--liveserver=superlists-52.78.139.60' in arg:
                cls.server_url = 'http://' + '--liveserver=superlists-52.78.139.60'[-12:]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    # @classmethod
    # def tearDownClass(cls):
    #     if cls.server_url == cls.live_server_url:
    #         super().tearDownClass()

    def setUp(self):
        # caps = DesiredCapabilities.FIREFOX
        # caps["marionette"] = True
        # caps["binary"] = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"
        #
        # self.browser = webdriver.Firefox(capabilities=caps)
        self.browser = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__)) + '/chromedriver_mac64/chromedriver')
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')