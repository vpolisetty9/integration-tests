from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AtsPage(BasePage):

    ats_link = (By.CSS_SELECTOR, '.navbar-right > li:nth-of-type(4) > a')
    add_a_candidate = (By.CSS_SELECTOR, '.btn-success')
    name_input = (By.CSS_SELECTOR, '#recruiter_update_name')
    save_changes_button = (By.CSS_SELECTOR, 'input[value="Save changes"]')
    success_message = (By.CSS_SELECTOR, '.alert-notice')
    edit_link = (By.CSS_SELECTOR, '.fa-pencil-square-o:nth-of-type(1)')
    click_to_add_link = (By.CSS_SELECTOR, '#main-content p:nth-of-type(1) > a')
    first_name = (By.CSS_SELECTOR, '#recruiter_update_first_name')
    check_mark = (By.CSS_SELECTOR, '.abracadabra-submit')