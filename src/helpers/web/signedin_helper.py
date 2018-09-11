from src.pages.signed_in_page import SignedinPage
import time

class SignedinHelper:

    signedin_page = SignedinPage()

    def verify_page(self):
        self.signedin_page.wait_for_page_load()

    def click_search_link(self):
        self.signedin_page.click_and_wait(self.signedin_page.search_link)

    def click_profile_link(self):
        self.signedin_page.click_and_wait(self.signedin_page.profile_link)

    def click_settings_link(self):
        self.signedin_page.click_and_wait(self.signedin_page.settings_link)
