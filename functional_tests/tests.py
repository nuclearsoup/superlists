# import time
from django.contrib.staticfiles.testing import StaticLiveServerCase
# from django.test import LiveServerTestCase
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(StaticLiveServerCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        ''' Go to webapge, ensure To-Do in title and heading
        '''
        self.browser.get(self.server_url)
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text

        self.assertIn('To-Do', header_text)
        
        # invited to add todo straight away

        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )

        # types buy peacock feathers into text to
        # when hits enter the page updates and the new page lists
        # "1: Buy peacock feathers" as an item in a to-do list table

        inputbox.send_keys('Buy peacock feathers')
 
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        
        # Being methodical she enters a second item:
        # Use feathers to make fly

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use feathers to make fly')
        inputbox.send_keys(Keys.ENTER)

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generate a unique URL for her -- there is some
        # explanatory text to that effect.

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use feathers to make fly')

        # Now a new user, Francis, comes along to the site.

        # We use a new browser session to ensure none of Edith's is
        # coming through from cookies etc.

        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the site, there is no sign of edith's list

        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Use feathers to make fly', page_text)

        # Francis starts a new list by entering an item

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own unique url.

        francis_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        # self.fail('Finish the test!')
        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

    def test_layout_and_styling(self):
        # Edith goes to the homepage
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)
        # She notices the inbox is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
            )
        # She starts a new list and notices the input is nicely cenred ther too
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
            )
if __name__ == '__main__':
    unittest.main(warnings='ignore')


