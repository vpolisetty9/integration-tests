from src.framework.base_test import BaseTest
from src.helpers.web.login_helper import LoginHelper
from src.helpers.web.signedin_helper import SignedinHelper
from src.helpers.utils_helper import UtilsHelper
from src.helpers.web.addprofile_helper import AddProfileHelper

class AddProfileTest(BaseTest):

    def setUp(self):
        super(AddProfileTest, self).setUp()

    def test_verify_guidelines(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        addprofile_helper = AddProfileHelper()

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Validate guidelines text
        signedin_helper.click_addprofile_link()
        addprofile_helper.verify_guidelines()

    def test_validate_error_alert_message(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        addprofile_helper = AddProfileHelper()

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Perform empty save profile
        signedin_helper.click_addprofile_link()
        addprofile_helper.click_save_profile()
        addprofile_helper.verify_alertdialog('Error Message')