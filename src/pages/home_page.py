from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    login_button = (By.CSS_SELECTOR, 'a[href="/users/sign_in"]')
    signup_button = (By.CSS_SELECTOR, 'a[href="/users/sign_up"]')