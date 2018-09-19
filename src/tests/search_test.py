from src.framework.base_test import BaseTest
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

    def test_job_title_search(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        search_helper = SearchHelper()
        job_title = 'CTO'

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Perform title search
        signedin_helper.click_search_link()
        search_helper.enter_job_title(job_title)
        search_helper.click_search_button()
        search_helper.verify_total_candidates_text()
        search_helper.validate_candidate_results_text(3)
        search_helper.validate_job_title(job_title)
        search_helper.click_search_result_by_index()

    def test_location_search(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        search_helper = SearchHelper()
        location = 'Texas'

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Perform location search
        signedin_helper.click_search_link()
        search_helper.enter_location(location)
        search_helper.click_search_button()
        search_helper.verify_total_candidates_text()
        search_helper.validate_candidate_results_text(5)
        search_helper.validate_job_title(location)
        search_helper.click_search_result_by_index()

    def test_skills_search(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        search_helper = SearchHelper()
        skills = 'java'

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Perform skills search
        signedin_helper.click_search_link()
        search_helper.enter_skills(skills)
        search_helper.click_search_button()
        search_helper.verify_total_candidates_text()
        search_helper.validate_candidate_results_text(10)
        search_helper.validate_skills(skills)
        search_helper.click_search_result_by_index()

    def test_companies_search(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        search_helper = SearchHelper()
        company = 'Amazon'

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Perform companies search
        signedin_helper.click_search_link()
        search_helper.enter_companies(company)
        search_helper.click_search_button()
        search_helper.verify_total_candidates_text()
        search_helper.validate_candidate_results_text(2)
        search_helper.click_search_result_by_index()

    def test_degrees_search(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        search_helper = SearchHelper()
        degrees = 'Bachelor of Engineering'

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Perform degrees search
        signedin_helper.click_search_link()
        search_helper.enter_degrees(degrees)
        search_helper.click_search_button()
        search_helper.verify_total_candidates_text()
        search_helper.validate_candidate_results_text(8)
        search_helper.click_search_result_by_index()

    def test_schools_search(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        search_helper = SearchHelper()
        schools = 'Sanjose University'

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Perform schools search
        signedin_helper.click_search_link()
        search_helper.enter_schools(schools)
        search_helper.click_search_button()
        search_helper.verify_total_candidates_text()
        search_helper.validate_candidate_results_text(2)
        search_helper.click_search_result_by_index()

    def test_keyword_search(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        search_helper = SearchHelper()
        keyword = 'Jobs1*'

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Perform keyword search
        signedin_helper.click_search_link()
        search_helper.enter_keyword(keyword)
        search_helper.click_search_button()
        search_helper.verify_total_candidates_text()
        search_helper.validate_candidate_results_text(7)
        search_helper.click_search_result_by_index()

    # def test_min_education_level_search(self):
    #     login_helper = LoginHelper()
    #     signedin_helper = SignedinHelper()
    #     search_helper = SearchHelper()
    #
    #     # Step1: Login as admin
    #     login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())
    #
    #     # Step2 : Perform min education level search
    #     signedin_helper.click_search_link()
    #     search_helper.select_min_education_level('Doctorate')
    #     search_helper.click_search_button()
    #     search_helper.verify_total_candidates_text()
    #     search_helper.validate_candidate_results_text(1)
    #     search_helper.click_search_result_by_index()

    def test_top_school_search(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        search_helper = SearchHelper()

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Perform top school search
        signedin_helper.click_search_link()
        search_helper.select_top_school()
        search_helper.click_search_button()
        search_helper.verify_total_candidates_text()
        search_helper.validate_candidate_results_text(8)
        search_helper.click_search_result_by_index()

    def test_top_company_search(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        search_helper = SearchHelper()

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Perform top company search
        signedin_helper.click_search_link()
        search_helper.select_top_company()
        search_helper.click_search_button()
        search_helper.verify_total_candidates_text()
        search_helper.validate_candidate_results_text(4)
        search_helper.click_search_result_by_index()

    def test_multiple_filters(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        search_helper = SearchHelper()
        job_title = 'CTO'
        location = 'Texas'

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Perform top company search
        signedin_helper.click_search_link()
        search_helper.enter_job_title(job_title)
        search_helper.enter_location(location)
        search_helper.click_search_button()
        search_helper.verify_total_candidates_text()
        search_helper.validate_candidate_results_text(2)
        search_helper.select_top_company()
        search_helper.click_search_button()
        search_helper.verify_total_candidates_text()
        search_helper.validate_candidate_results_text(2)
        search_helper.click_search_result_by_index()

    def test_non_matching_search(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        search_helper = SearchHelper()
        job_title = 'ABCD'
        location = 'Mountain View'

        # Step1: Login as admin
        login_helper.login(UtilsHelper.get_admin_user(), UtilsHelper.get_admin_password())

        # Step2 : Perform top company search
        signedin_helper.click_search_link()
        search_helper.enter_job_title(job_title)
        search_helper.enter_location(location)
        search_helper.click_search_button()
        search_helper.validate_no_candidate_results_text()
        search_helper.select_top_company()
        search_helper.select_top_school()
        search_helper.click_search_button()
        search_helper.validate_no_candidate_results_text()