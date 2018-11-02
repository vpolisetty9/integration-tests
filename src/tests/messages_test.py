from src.framework.base_test import BaseTest
from src.helpers.web.login_helper import LoginHelper
from src.helpers.web.messages_helper import MessagesHelper
from src.helpers.utils_helper import UtilsHelper

class MessagesTest(BaseTest):

    def setUp(self):
        super(MessagesTest, self).setUp()

    def test_send_message(self):
        login_helper = LoginHelper()
        messages_helper = MessagesHelper()

        # Login as job seeker
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Click on Messages link
        messages_helper.click_messages_link()

        # Click on new message link
        messages_helper.click_new_message_link()

        # Enter email input
        #message_helper.enter_to_input("test@example.com")

        # Enter Subject input
        messages_helper.enter_subject_input("Subject")

        # Enter Message input
        messages_helper.enter_message_input("Message")

        # Click on Send button
        messages_helper.click_send_button()

