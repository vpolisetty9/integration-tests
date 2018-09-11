from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):

    search_button = (By.CSS_SELECTOR, '#new_search input[type="submit"]')
    cancel_button = (By.CSS_SELECTOR, '#new_search input[type="cancel"]')
    keyword_input = (By.CSS_SELECTOR, '#new_search #search_keyword')
    skills_input = (By.CSS_SELECTOR, '#new_search #search_skills')
    locations_input = (By.CSS_SELECTOR, '#new_search #search_locations')
    school_input = (By.CSS_SELECTOR, '#new_search #search_schools')
    disciplines_input = (By.CSS_SELECTOR, '#new_search #search_disciplines')
    degrees_input = (By.CSS_SELECTOR, '#new_search #search_degrees')
    employers_input =(By.CSS_SELECTOR,  '#new_search #search_employers')
    names_input = (By.CSS_SELECTOR, '#new_search #search_names')
    titles_input = (By.CSS_SELECTOR, '#new_search #search_titles')
    experiences_input = (By.CSS_SELECTOR, '#new_search #search_experience_years')
    fulltime_checkbox = (By.CSS_SELECTOR, '#new_search #search_job_type_full_time')
    contract_checkbox = (By.CSS_SELECTOR, '#new_search #search_job_type_contract')
    relocate_checkbox = (By.CSS_SELECTOR, '#new_search #search_relocation')
    remote_checkbox = (By.CSS_SELECTOR, '#new_search #search_remote')
    recently_joined_checkbox = (By.CSS_SELECTOR, '#new_search #search_recently_added')

    # search results elements
    total_candidates_text = (By.CSS_SELECTOR, '.total-candidates')
    candidate_title = (By.CSS_SELECTOR, '.grid-candidate .employer_candidate_title > a')