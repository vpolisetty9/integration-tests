from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MessagesPage(BasePage):

    messages_link = (By.CSS_SELECTOR, '.navbar-left > li:nth-of-type(3) > a')
    new_message_link = (By.CSS_SELECTOR, 'a[href="/messages/new"]')
    to_input = (By.CSS_SELECTOR, '.chosen-search-input')
    subject_input = (By.CSS_SELECTOR, '#message_subject')
    message_input = (By.CSS_SELECTOR, '#message_body')
    send_button = (By.CSS_SELECTOR, 'input[value="Send"]')
