from src.pages.add_profile_page import AddProfilePage

class AddProfileHelper:

    addprofile_page = AddProfilePage()

    def verify_alertdialog(self, expected_message):
        self.addprofile_page.is_element_displayed(self.addprofile_page.alert_message)
        actual_message = self.addprofile_page.get_text(self.addprofile_page.alert_message)
        assert expected_message in actual_message, 'Alert message mismatch'

    def click_save_profile(self):
        self.addprofile_page.click(self.addprofile_page.save_button)

    def verify_guidelines(self):
        self.addprofile_page.is_element_displayed(self.addprofile_page.guidelines_header)
        actual_text = self.addprofile_page.get_text(self.addprofile_page.guidelines_header)
        expected_text = 'Guidelines for inputting candidate information'
        assert expected_text == actual_text, 'Guidelines header text did not match'

        expected_list = [
            '1. Make sure ALL information is accurate!',
            '2. Don\'t use special formatting. If you must copy-paste information, always \'paste as plain text.\'',
            '3. Name, email address, and phone number are required.',
            '4. Document/resume is required only if LinkedIn profile URL is blank.'
        ]
        elements = self.addprofile_page.find_elements(self.addprofile_page.guidelines_list)

        for titles in range(len(elements)):
            assert expected_list[titles] == elements[titles].text
