from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TalentProfilePage(BasePage):
    social_container = (By.CSS_SELECTOR, '.socials-container')
    social_media_button = (By.CSS_SELECTOR, '.social-media-btn')

    education_grid = (By.CSS_SELECTOR, '.grid-education')
    education_icon = (By.CSS_SELECTOR, ".education-icon")
    education_info = (By.CSS_SELECTOR, '.grid-education .education-icon + div div:nth-of-type(1)')
    education_university = (By.CSS_SELECTOR, '.grid-education .education-icon + div div:nth-of-type(2)')
    location_row = (By.CSS_SELECTOR, ".location-row")
    location_icon = (By.CSS_SELECTOR, ".location-icon")

    profile_pic_container = (By.CSS_SELECTOR, ".profile-pic-container")
    profile_pic = (By.CSS_SELECTOR, ".profile-pic")
    profile_btn_background =(By.CSS_SELECTOR, ".profile-btn-background")
    user_info = (By.CSS_SELECTOR, ".grid-name .user-info")
    experience_type = (By.CSS_SELECTOR, ".grid-experience div:nth-of-type(1)")
    experience_years = (By.CSS_SELECTOR, ".grid-experience div:nth-of-type(2)")

    salary_grid = (By.CSS_SELECTOR, ".grid-salary")
    expected_salary = (By.CSS_SELECTOR, ".grid-salary div:nth-of-type(1) div")
    profile_status = (By.CSS_SELECTOR, ".status-update")
    profile_glider = (By.CSS_SELECTOR, ".grid-status-slider span")

    employer_grid = (By.CSS_SELECTOR, ".grid-employers")

    contact_grid = (By.CSS_SELECTOR, ".grid-contact")
    email_title = (By.CSS_SELECTOR, ".grid-email .title")
    email_text = (By.CSS_SELECTOR, ".grid-email .user-info")
    phone_title = (By.CSS_SELECTOR, ".grid-phone .title")
    phone_text = (By.CSS_SELECTOR, ".grid-phone .user-info")
    address_title = (By.CSS_SELECTOR, ".grid-address .title")
    address_text = (By.CSS_SELECTOR, ".grid-address .user-info")
    city_title = (By.CSS_SELECTOR, ".grid-city .title")
    city_text = (By.CSS_SELECTOR, ".grid-city .user-info")
    state_title = (By.CSS_SELECTOR, ".grid-state .title")
    state_text = (By.CSS_SELECTOR, ".grid-state .user-info")
    zipcode_title = (By.CSS_SELECTOR, ".grid-zipcode .title")
    zipcode_text = (By.CSS_SELECTOR, ".grid-zipcode .user-info")
    edit_contact = (By.CSS_SELECTOR, ".grid-contact .edit-icon")

    profile_background_grid = (By.CSS_SELECTOR, ".grid-contact + .row-special")
    upcoming_title = (By.CSS_SELECTOR, ".upcoming .grid-title")
    upcoming_text = (By.CSS_SELECTOR, ".upcoming .upcoming-box")
    quick_reply_title = (By.CSS_SELECTOR, ".quick-reply .grid-title")
    quick_reply_text = (By.CSS_SELECTOR, ".quick-reply .quick-reply-box")
    about_title = (By.CSS_SELECTOR, ".grid-intro .grid-title")
    about_text = (By.CSS_SELECTOR, ".grid-intro .grid-content")
    skills_title = (By.CSS_SELECTOR, ".grid-skills .grid-title")
    skills_text = (By.CSS_SELECTOR, ".grid-skills .user-skills")
    experience_title = (By.CSS_SELECTOR, ".grid-experience2 .grid-title")
    experience_section = (By.CSS_SELECTOR, ".grid-experience2 ul li")
    experience_main_title = (By.CSS_SELECTOR, ".grid-experience2 ul li:nth-of-type(1) .experience-title")
    experience_sub_title = (By.CSS_SELECTOR, ".grid-experience2 ul li:nth-of-type(1) .experience-sub-title")
    experience_duration = (By.CSS_SELECTOR, ".grid-experience2 ul li:nth-of-type(1) .experience-duration")
    education_title = (By.CSS_SELECTOR, ".grid-education2 .grid-title")
    education_icon = (By.CSS_SELECTOR, ".education-row .education-icon")
    degree_name = (By.CSS_SELECTOR, ".education-row .education-icon + div div:nth-of-type(1)")
    degree_type = (By.CSS_SELECTOR, ".education-row .education-icon + div div:nth-of-type(2)")
    degree_university = (By.CSS_SELECTOR, ".education-row .education-icon + div div:nth-of-type(3)")

    # award elements are pending

    interview_requests_title = (By.CSS_SELECTOR, ".grid-interview .grid-title")
    interview_box = (By.CSS_SELECTOR, ".interview-box")

    questions_title = (By.CSS_SELECTOR, ".grid-questions .grid-title")
    account_manager_img = (By.CSS_SELECTOR, ".grid-questions .acc-manager-pic")
    account_manager_text = (By.CSS_SELECTOR, ".grid-questions .acc-manager-pic + div")
    questions_box = (By.CSS_SELECTOR, ".questions-box")
    questions_send_button = (By.CSS_SELECTOR, ".questions-box + .send-btn")

    portfolio_title = (By.CSS_SELECTOR, ".grid-portfolio .grid-title")
    portfolio_add = (By.CSS_SELECTOR, ".grid-portfolio .grid-add")
    portfolio_app = (By.CSS_SELECTOR, ".grid-portfolio .grid-app")
    portfolio_template_box = (By.CSS_SELECTOR, ".grid-portfolio .grid-app:nth-child(3) #template-box-1")
