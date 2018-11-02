from src.pages.ats_page import AtsPage
import time
import src.framework.config as config
from selenium.webdriver.support.ui import Select

class AtsHelper:

    ats_page = AtsPage()

    def verify_page(self):
        self.ats_page.wait_for_page_load()

    # Add candidate scenario

    def click_ats_link(self):
        self.ats_page.click_and_wait(self.ats_page.ats_link)

    def click_add_a_candidate_button(self):
        self.ats_page.click_and_wait(self.ats_page.add_a_candidate)

    def enter_name_input(self, name):
        self.ats_page.type(self.ats_page.name_input, name)

    def click_save_changes_button(self):
        self.ats_page.click_and_wait(self.ats_page.save_changes_button)

    def verify_success_message(self):
        self.ats_page.is_element_displayed(self.ats_page.success_message)

    # Edit candidate scenario

    def click_edit_link(self):
        self.ats_page.click_and_wait(self.ats_page.edit_link)

    def click_to_add_link(self):
        self.ats_page.click_and_wait(self.ats_page.click_to_add_link)

    def enter_first_name(self, fname):
        self.ats_page.clear(self.ats_page.first_name)
        self.ats_page.type(self.ats_page.first_name, fname)

    def click_check_mark(self):
        self.ats_page.click_and_wait(self.ats_page.check_mark)

    def verify_updated_data(self, fname):
        text = self.ats_page.get_text(self.ats_page.click_to_add_link)
        assert text == fname

    # Delete candidate scenario
