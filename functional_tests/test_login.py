from .base import FunctionalTest
import time
TEST_EMAIL = 'edith@mockmyid.com'


class LoginTest(FunctionalTest):

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')


    def test_login_with_persona(self):
        # Edith goes to to site and notices login link
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click()
        # A persona login window appearsa
        self.switch_to_new_window('Mozilla Persona')
        # Edith signs in with her email address
        # use mockmyid.com for test email
        self.browser.find_element_by_id(
            'authentication_email'
            ).send_keys(TEST_EMAIL)
        self.browser.find_element_by_tag_name('button').click()

        # The persona window closes
        self.switch_to_new_window('To-Do')

        # She can see that she is logged in
        self.wait_to_be_logged_in(email=TEST_EMAIL)
        # Refreshing the page,
        self.browser.refresh()
        # She can see that it is a real session
        self.wait_to_be_logged_in(email=TEST_EMAIL)

        # Terrified of this new feature she clicks logout
        self.browser.find_element_by_id('id_logout').click()
        self.wait_to_be_logged_out(email=TEST_EMAIL)

        # And then check to see if the logged out state persists
        self.browser.refresh()
        self.wait_to_be_logged_out(email=TEST_EMAIL)
