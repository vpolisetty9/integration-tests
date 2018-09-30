from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SignedinPage(BasePage):
    logout = (By.CSS_SELECTOR, 'a[href="/users/sign_out"]')
    dashboard_link = (By.CSS_SELECTOR, '#custom_navbar .navbar-right li:nth-of-type(1) a')
    add_profile_link = (By.CSS_SELECTOR, 'a[href="/people/new"]')
    settings_link = (By.CSS_SELECTOR, 'a[href="/users/edit"]')
    profile_link = (By.CSS_SELECTOR, 'a[href="/welcome/talent_intro"]')
    search_link = (By.CSS_SELECTOR, 'a[href="/searches/new"]')