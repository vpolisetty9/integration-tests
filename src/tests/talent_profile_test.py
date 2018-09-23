from src.framework.base_test import BaseTest
from src.helpers.web.login_helper import LoginHelper
from src.helpers.web.signedin_helper import SignedinHelper
from src.helpers.web.talentprofile_helper import TalentProfileHelper

class TalentProfileTest(BaseTest):

    def setUp(self):
        super(TalentProfileTest, self).setUp()

    def test_verify_talent_profile(self):
        login_helper = LoginHelper()
        signedin_helper = SignedinHelper()
        talent_profile_helper = TalentProfileHelper()
        user_objs = {
            'jobseeker1': {
                'email': "jobseekercardinal+3@gmail.com",
                'password': "qwerty123",
                'first_name': "jobseeker",
                'last_name': "cardinal",
                'full_name': "Jobseeker Cardinal",
                'phone': "123456789",
                'address': "QWERTY456 QWERTY123",
                'city': "San Francisco",
                'state': "California",
                'zipcode': "93004",
                'expected_salary': "$150,000 - $200,000",
                'interested_in': "Technology",
                'degree': "Bachelors",
                'degree_type': "Computers",
                'university': "Stanford University (2008)",
                'experience': "0-1",
                'skills': "Java, Javascript, Node.js, C",
                'interested_job_type': "remote",
                'interested_locations': "San Francisco, San Diego and San Jose"
            }
        }

        user_obj = user_objs['jobseeker1']

        # Step1: Login as admin
        login_helper.login(user_obj['email'], user_obj['password'])

        # Step2 : verify talent profile elements & values
        signedin_helper.click_profile_link()
        talent_profile_helper.verfify_social_container()
        talent_profile_helper.verify_social_container_elements()
        talent_profile_helper.verify_education_elements()
        talent_profile_helper.validate_education(user_obj)
        talent_profile_helper.verify_location_elements()
        talent_profile_helper.validate_location(user_obj)
        talent_profile_helper.verify_location_elements()
        talent_profile_helper.validate_experience(user_obj)
        talent_profile_helper.verify_salary_elements()
        talent_profile_helper.validate_salary_section(user_obj)
        talent_profile_helper.validate_contact_section(user_obj)
        talent_profile_helper.verify_profile_background_elements()
        talent_profile_helper.validate_about_experience(user_obj)
        talent_profile_helper.validate_skills(user_obj)
        talent_profile_helper.validate_education(user_obj)