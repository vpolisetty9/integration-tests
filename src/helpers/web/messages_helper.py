from src.pages.messages_page import MessagesPage


class MessagesHelper:

    messages_page = MessagesPage()

    def verify_page(self):
        self.messages_page.wait_for_page_load()

    def click_messages_link(self):
        self.messages_page.click_and_wait(self.messages_page.messages_link)

    def click_new_message_link(self):
        self.messages_page.click_and_wait(self.messages_page.new_message_link)

    def enter_to_input(self, email):
        self.messages_page.type(self.messages_page.to_input, email)

    def enter_subject_input(self, subject):
        self.messages_page.type(self.messages_page.subject_input, subject)

    def enter_message_input(self, message):
        self.messages_page.type(self.messages_page.message_input, message)

    def click_send_button(self):
        self.messages_page.click_and_wait(self.messages_page.send_button)
