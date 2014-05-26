from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Mistakenly enters blank object
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        # Page refreshes telling her entry cannot be empty
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        # Try again with test for item which now succeeds
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')
        # Perversely do same again and receives similar warning on list page.
        self.get_item_input_box().send_keys('\n')
        # And she can correct by filling some test in
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')


    def test_cannot_add_duplicate_items(self):
        # Goes to main page, starts new list

        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        # Accidentally tries to enter duplicate entry

        self.get_item_input_box().send_keys('Buy wellies\n')

        # Sees helpful error message

        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You've already got this in your list")

if __name__ == '__main__':
    unittest.main(warnings='ignore')
