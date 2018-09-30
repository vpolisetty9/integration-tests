from src.pages.search_page import SearchPage
import time
import src.framework.config as config
from selenium.webdriver.support.ui import Select

class SearchHelper:

    search_page = SearchPage()

    def verify_page(self):
        self.search_page.wait_for_page_load()

    def click_search_button(self):
        self.search_page.click_and_wait(self.search_page.search_button)

    def click_top_search_button(self):
        self.search_page.click_and_wait(self.search_page.search_top_button)

    def verify_total_candidates_text(self):
        self.search_page.wait_for_presence(self.search_page.total_candidates_text)

    def validate_candidate_results_text(self, expected_results_count):
        actual_text = self.search_page.get_text(self.search_page.total_candidates_text)
        assert 'No Matching Candidates Found' != actual_text
        elements = self.search_page.find_elements(self.search_page.candidate_grid)
        if len(elements) > 1:
            expected_text = 'Displaying All ' + str(len(elements)) + ' Matching Candidates'
        else:
            expected_text = 'Displaying ' + str(len(elements)) + ' Matching Candidate'
        assert expected_text == actual_text
        assert str(expected_results_count) == str(len(elements))

    def validate_no_candidate_results_text(self):
        actual_text = self.search_page.get_text(self.search_page.total_candidates_text)
        assert 'No Matching Candidates Found' == actual_text
        self.search_page.wait_for_element_not_to_be_present(self.search_page.candidate_grid)

    def validate_job_title(self, expected_title):
        elements = self.search_page.find_elements(self.search_page.candidate_job_title)
        for title in range(len(elements)):
            assert expected_title in elements[title].text

    def validate_skills(self, expected_text):
        elements = self.search_page.find_elements(self.search_page.candidate_skills)
        for title in range(len(elements)):
            assert expected_text in elements[title].text

    def click_search_result_by_index(self, index=0):
        self.search_page.click_elements_by_index(self.search_page.candidate_title, index)

    def enter_top_keyword(self, keyword_text):
        self.search_page.is_element_displayed(self.search_page.top_search_input)
        self.search_page.is_element_displayed(self.search_page.search_top_button)
        self.search_page.clear(self.search_page.top_search_input)
        self.search_page.type(self.search_page.top_search_input, keyword_text)

    def enter_job_title(self, job_title):
        self.search_page.is_element_displayed(self.search_page.label_titles)
        self.search_page.click(self.search_page.titles_button)
        self.search_page.type(self.search_page.titles_input, job_title)

    def enter_location(self, location):
        self.search_page.is_element_displayed(self.search_page.label_locations)
        self.search_page.click(self.search_page.locations_button)
        self.search_page.type(self.search_page.locations_input, location)

    def enter_skills(self, skills):
        self.search_page.is_element_displayed(self.search_page.label_skills)
        self.search_page.click(self.search_page.skills_button)
        self.search_page.type(self.search_page.skills_input, skills)

    def enter_companies(self, text):
        self.search_page.is_element_displayed(self.search_page.label_employers)
        self.search_page.click(self.search_page.employers_button)
        self.search_page.type(self.search_page.employers_input, text)

    def enter_degrees(self, text):
        self.search_page.is_element_displayed(self.search_page.label_disciplines)
        self.search_page.click(self.search_page.disciplines_button)
        self.search_page.type(self.search_page.disciplines_input, text)

    def enter_schools(self, text):
        self.search_page.is_element_displayed(self.search_page.label_schools)
        self.search_page.click(self.search_page.schools_button)
        self.search_page.type(self.search_page.school_input, text)

    def enter_keyword(self, text):
        self.search_page.is_element_displayed(self.search_page.label_keyword)
        self.search_page.click(self.search_page.keyword_button)
        self.search_page.type(self.search_page.keyword_input, text)

    def select_top_school(self):
        self.search_page.click(self.search_page.top_school_checkbox)

    def select_top_company(self):
        self.search_page.click(self.search_page.top_company_checkbox)

    def select_active_profiles(self):
        self.search_page.click(self.search_page.active_profile_checkbox)

    def select_avail_phone_num(self):
        self.search_page.click(self.search_page.avail_phone_number_checkbox)

    def select_avail_email(self):
        self.search_page.click(self.search_page.avail_email_checkbox)

    def select_min_education_level(self, text):
        self.search_page.click(self.search_page.min_education_level)
        drop_down = Select(self.search_page.min_education_level)
        drop_down.select_by_visible_text(text)

    def reset_all_filters(self):
        self.search_page.clear(self.search_page.titles_input)
        self.search_page.clear(self.search_page.locations_input)
        self.search_page.clear(self.search_page.skills_input)