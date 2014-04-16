from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        ''' Go to webapge, ensure To-Do in title and heading
        '''
        self.browser.get('http://localhost:8000')
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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # Being methodical she enters a second item:
        # Use feathers to make fly

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use feathers to make fly')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use feathers to make fly',
            [row.text for row in rows]
            )

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
