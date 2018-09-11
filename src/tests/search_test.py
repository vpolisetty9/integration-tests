from src.framework.base_test import BaseTest
from src.helpers.web.home_helper import HomeHelper
from src.helpers.web.login_helper import LoginHelper
from src.helpers.web.signedin_helper import SignedinHelper
from src.helpers.utils_helper import UtilsHelper
from src.helpers.web.search_helper import SearchHelper

class SearchTest(BaseTest):

    def setUp(self):
        super(SearchTest, self).setUp()

    def test_default_search(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        search_helper = SearchHelper()

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Perform null search
        signedin_helper.click_search_link()
        search_helper.click_search_button()
        search_helper.click_search_result_by_index()
