from src.framework.base_test import BaseTest
from src.helpers.web.login_helper import LoginHelper
from src.helpers.web.ats_helper import AtsHelper
from src.helpers.utils_helper import UtilsHelper

class AtsTest(BaseTest):

    def setUp(self):
        super(AtsTest, self).setUp()

    def test_default_add_candidate(self):
        login_helper = LoginHelper()
        ats_helper = AtsHelper()

        # Login as admin
        login_helper.login(UtilsHelper.get_recruiter_user(), UtilsHelper.get_recruiter_password())

        # Click ATS link
        ats_helper.click_ats_link()

        # Click Add a Candidate button
        ats_helper.click_add_a_candidate_button()

        # Enter name input
        ats_helper.enter_name_input("Cardinal")

        # Click on Save Changes button
        ats_helper.click_save_changes_button()

        # Verify Success confirmation message
        ats_helper.verify_success_message()

    def test_default_edit_candidate(self):
        login_helper = LoginHelper()
        ats_helper = AtsHelper()

        # Login as admin
        login_helper.login(UtilsHelper.get_recruiter_user(), UtilsHelper.get_recruiter_password())

        # Click ATS link
        ats_helper.click_ats_link()

        # Click Edit link
        ats_helper.click_edit_link()

        # Click 'Click to Add' link
        ats_helper.click_to_add_link()

        # Enter first name
        ats_helper.enter_first_name("First Name")

        # Click on Check mark
        ats_helper.click_check_mark()

        # Verify Success confirmation message
        ats_helper.verify_updated_data("First Name")