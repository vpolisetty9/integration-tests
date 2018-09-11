from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SignupPage(BasePage):

    preloader = (By.CSS_SELECTOR, '#preloader')
    login_button = (By.CSS_SELECTOR, '.img__btn')
    signin_user_email =  (By.CSS_SELECTOR, 'form[action="/users/sign_in"] #user_email')
    signin_user_password = (By.CSS_SELECTOR, 'form[action="/users/sign_in"] #user_password')
    signin_button =  (By.CSS_SELECTOR, 'form[action="/users/sign_in"] input[name="commit"]')
    alert_error = (By.CSS_SELECTOR, '.alert.alert-alert')
    error_explanation = (By.CSS_SELECTOR, '#error_explanation')

    signup_user_email = (By.CSS_SELECTOR, 'form[action="/users"] #user_email')
    signup_user_password = (By.CSS_SELECTOR, 'form[action="/users"] #user_password')
    signup_button = (By.CSS_SELECTOR, 'form[action="/users"] input[name="commit"]')

    # Step one elements

    # index values: 'talent', employer, recruiter
    roles_buttons_by_index = (By.CSS_SELECTOR, '#{}')
    role_next_button = (By.CSS_SELECTOR, '.btn.btn-blue[value="Next"]')

    # Step two elements
    firstname_input = (By.CSS_SELECTOR, '.edit_user #first_name')
    lastname_input = (By.CSS_SELECTOR, '.edit_user #last_name')
    phonenumber_input = (By.CSS_SELECTOR, '.edit_user #phone_number')
    remote_input = (By.CSS_SELECTOR, '.edit_user #remote')
    address1_input = (By.CSS_SELECTOR, '.edit_user #address_1')
    address2_input = (By.CSS_SELECTOR, '.edit_user #address_2')
    city_input = (By.CSS_SELECTOR, '.edit_user #city')
    state_input = (By.CSS_SELECTOR, '.edit_user #state')
    zipcode_input = (By.CSS_SELECTOR, '.edit_user #zipcode')
    steptwo_next_button = (By.CSS_SELECTOR, '.btn.btn-blue[value="Next"]')

    # Step three elements

    # index values : zero_one, one_two, two_four, four_five, six_plus
    experience_buttons_by_index = (By.CSS_SELECTOR, 'label[for="user[experience_years][{}]"]')

    #index values: Back_End, Front_End, Mobile_Dev
    fulltime_roles_held_by_index = (By.CSS_SELECTOR, 'label[for="user[roles_held][{}]')

    # index values: Anroid, Angular_JS, Automation_Testing
    strongest_skills_by_index = (By.CSS_SELECTOR, 'label[for="user[skills][{}]"')

    #index values: Back_End_Engineer, Data_Science,
    roles_interested_by_index = (By.CSS_SELECTOR, 'label[for="user[roles_interested][\'{}\']"]')
    stepthree_next_button = (By.CSS_SELECTOR, 'form[action="/after_signup/step_three"] input[type="submit"]')



    # Step4 Elements
    # index values: permanent, contract, remote
    employment_sought_by_index =  (By.CSS_SELECTOR, 'label[for="user[employment_sought][{}]"]')
    desired_salary_by_index = (By.CSS_SELECTOR, '{}')

    #index values: active, passive, inactive
    job_search_stage_by_index = (By.CSS_SELECTOR, 'label[for="user[job_search_stage][{}]"]')

    stepfour_finish_button = (By.CSS_SELECTOR, 'form[action="/after_signup/step_four"] input[value="Finish"]')
