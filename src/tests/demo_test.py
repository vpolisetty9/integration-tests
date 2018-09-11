from src.framework.base_test import BaseTest
from src.helpers.web.home_helper import HomeHelper

class DemoTest(BaseTest):

    def setUp(self):
        super(DemoTest, self).setUp()

    def test_one(self):
        home_helper = HomeHelper()
        home_helper.visit_page()
        home_helper.click_get_estimate_button()