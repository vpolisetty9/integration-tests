from src.pages.talent_profile_page import TalentProfilePage
from selenium.webdriver.common.by import By

class TalentProfileHelper:

    talentprofile_page = TalentProfilePage()

    def verfify_social_container(self):
        self.talentprofile_page.wait_for_presence(self.talentprofile_page.social_container)

    def verify_social_container_elements(self):
        elements = self.talentprofile_page.find_elements(self.talentprofile_page.social_media_button)
        media_buttons = ["facebook", "twitter", "linkedin", "behance", "dribble", "github"]
        assert len(media_buttons) == len(elements), "Social Media buttons count mismatch"
        for items in media_buttons:
            assert self.talentprofile_page.is_element_displayed((By.CSS_SELECTOR, '.' + str(items))), "Social media button" + items + "not found"

    def verify_education_elements(self):
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.education_grid)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.education_icon)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.education_info)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.education_university)

    def validate_education(self, user_obj):
        actual_education_info = self.talentprofile_page.get_text(self.talentprofile_page.education_info)
        expected_education_info = user_obj['degree_type'] + ", " + user_obj['degree']
        assert expected_education_info in actual_education_info, "Education info didn't match"

        actual_education_university = self.talentprofile_page.get_text(self.talentprofile_page.education_university)
        expected_education_university = user_obj['university']
        assert expected_education_university in actual_education_university, "University didn't match"

    def verify_location_elements(self):
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.location_icon)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.location_row)

    def validate_location(self, user_obj):
        actual_location_info = self.talentprofile_page.get_text(self.talentprofile_page.location_row)
        expected_location_info = user_obj['city'] + ", " + user_obj['state']
        assert expected_location_info in actual_location_info, "Location info didn't match"

    def verify_location_elements(self):
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.profile_pic_container)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.profile_pic)
        #self.talentprofile_page.is_element_displayed(self.talentprofile_page.profile_btn_background)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.user_info)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.experience_type)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.experience_years)

    def validate_experience(self, user_obj):
        actual_full_name = self.talentprofile_page.get_text(self.talentprofile_page.user_info)
        expected_full_name = user_obj['full_name']
        assert expected_full_name in actual_full_name, "Full name info didn't match"

        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.experience_type)
        expected_txt = "Interested in "+ user_obj['interested_in']
        assert expected_txt in actual_txt, "Interested in info didn't match"

        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.experience_years)
        expected_txt = user_obj['experience'] + " Years of Experience"
        assert expected_txt in actual_txt, "Experience info didn't match"

    def verify_salary_elements(self):
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.salary_grid)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.expected_salary)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.profile_status)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.profile_glider)

    def validate_salary_section(self, user_obj):
        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.expected_salary)
        expected_txt = user_obj['expected_salary'] + " Salary"
        assert expected_txt in actual_txt, "Expected Salary info didn't match"

        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.profile_status)
        expected_txt = "OPEN TO NEW OPPORTUNITIES"
        assert expected_txt in actual_txt, "Opportunities Status in info didn't match"

        self.talentprofile_page.click(self.talentprofile_page.profile_glider)

        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.profile_status)
        expected_txt = "INACTIVE PROFILE"
        assert expected_txt in actual_txt, "Opportunities Status in info didn't match"

        self.talentprofile_page.click(self.talentprofile_page.profile_glider)

        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.profile_status)
        expected_txt = "OPEN TO NEW OPPORTUNITIES"
        assert expected_txt in actual_txt, "Opportunities Status in info didn't match"

    def validate_contact_section(self, user_obj):
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.contact_grid)

        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.email_text)
        expected_txt = user_obj['email']
        assert expected_txt in actual_txt, "Email info didn't match"

        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.phone_text)
        expected_txt = user_obj['phone']
        assert expected_txt in actual_txt, "Phone numbers didn't match"

        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.address_text)
        expected_txt = user_obj['address']
        assert expected_txt in actual_txt, "Address didn't match"

        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.city_text)
        expected_txt = user_obj['city']
        assert expected_txt in actual_txt, "City didn't match"

        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.state_text)
        expected_txt = user_obj['state']
        assert expected_txt in actual_txt, "state didn't match"

        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.zipcode_text)
        expected_txt = user_obj['zipcode']
        assert expected_txt in actual_txt, "zipcode didn't match"

        self.talentprofile_page.is_element_displayed(self.talentprofile_page.edit_contact)

    def verify_profile_background_elements(self):
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.upcoming_text)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.upcoming_title)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.quick_reply_title)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.quick_reply_text)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.interview_requests_title)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.interview_box)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.questions_title)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.account_manager_img)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.account_manager_text)
        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.account_manager_text)
        expected_txt = "Send a message to Daniel Parillo, your account manager."
        assert expected_txt in actual_txt, "Account Manager Text didn't match"
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.questions_box)
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.questions_send_button)

    def validate_about_experience(self, user_obj):
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.about_text)
        if user_obj['interested_job_type'] == 'remote':
            location = 'remotely'
        actual_txt = self.talentprofile_page.get_text(self.talentprofile_page.about_text)
        expected_txt = "Hi, my name is " + user_obj['full_name'] + ", and I'm currently interested in a " + user_obj['interested_in'] + " position. I'm currently actively searching for a " + user_obj['interested_job_type'] + " job position. The locations I'm interested in working at include " + user_obj['interested_locations'] + ". I am currently interested in working " + location + "."
        assert expected_txt in actual_txt, "About Text didn't match"

    def validate_skills(self, user_obj):
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.skills_text)
        elements = self.talentprofile_page.find_elements(self.talentprofile_page.skills_text)
        for skills in elements:
            assert skills.text in user_obj['skills'], "Skills didn't match"

    def validate_education(self, user_obj):
        self.talentprofile_page.is_element_displayed(self.talentprofile_page.education_icon)
        actual_education_info = self.talentprofile_page.get_text(self.talentprofile_page.degree_name)
        expected_education_info = user_obj['degree']
        assert expected_education_info in actual_education_info, "Degree didn't match"

        actual_education_info = self.talentprofile_page.get_text(self.talentprofile_page.degree_type)
        expected_education_info = user_obj['degree_type']
        assert expected_education_info in actual_education_info, "Degree type didn't match"

        actual_education_university = self.talentprofile_page.get_text(self.talentprofile_page.degree_university)
        expected_education_university = user_obj['university']
        assert expected_education_university in actual_education_university, "University didn't match"