from src.pages.signup_page import SignupPage
import time


class LoginHelper:

    signup_page = SignupPage()

    def visit_login_page(self):
        self.signup_page.open_url(self.signup_page.APP_URL + "users/sign_in")
        self.verify_page()

    def verify_page(self):
        self.signup_page.find_element(self.signup_page.signin_button)
        # with self.signup_page.wait_for():
        #     self.signup_page.find_element(self.signup_page.signin_button)

    def enter_email_address(self, email):
        self.signup_page.type(self.signup_page.signin_user_email, email)

    def enter_password(self, password):
        self.signup_page.type(self.signup_page.signin_user_password, password)

    def click_login_button(self):
        self.signup_page.wait_for_presence(self.signup_page.signin_button)
        self.signup_page.click_and_wait(self.signup_page.signin_button)

    def login(self, email, password):
        self.visit_login_page()
        self.enter_email_address(email)
        self.enter_password(password)
        self.click_login_button()