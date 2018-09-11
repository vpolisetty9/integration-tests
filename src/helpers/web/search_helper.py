from src.pages.search_page import SearchPage
import time
import src.framework.config as config

class SearchHelper:

    search_page = SearchPage()

    def verify_page(self):
        self.search_page.wait_for_page_load()

    def click_search_button(self):
        self.search_page.click_and_wait(self.search_page.search_button)

    def verify_total_candidates_text(self):
        self.search_page.wait_for_presence(self.search_page.total_candidates_text)

    def click_search_result_by_index(self, index=0):
        self.search_page.click_elements_by_index(self.search_page.candidate_title, index)