from src.pages.home_page import HomePage

class HomeHelper:

    home_page = HomePage()

    def visit_page(self):
        self.home_page.open_url(self.home_page.APP_URL)
        self.verify_page()

    def verify_page(self):
        self.home_page.find_element(self.home_page.login_button)

    def click_login_button(self):
        self.home_page.click_and_wait(self.home_page.login_button)

    def click_signup_button(self):
        self.home_page.click_and_wait(self.home_page.signup_button)