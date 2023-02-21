import allure
import pytest
from Web.base.BasePage import BasePage
from Web.pages.ContactUsPage import ContactUsPage


class TestContactUs(ContactUsPage, BasePage):
    def handling_the_first_popup(self):
        self.open()
        self.selecting_option_one()
        self.selecting_option_two()
        self.click_save_button()

    @allure.description("Verify if we can send a message with  all valid data")
    def test_all_valid_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.success_message_xpath) == "הפרטים נקלטו בהצלחה"
        self._driver.close()

    @allure.description("Verifying that we can not send messages with empty first name")
    def test_empty_first_name_value(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.empty_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verify_the_title_of_the_page() == 'שירות לקוחות'
        assert self.indication_alert(self.indication_message_xpath) == "נא למלא שדה זה"
        self._driver.close()

    @allure.description("Test empty last name")
    def test_empty_last_name_value(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.empty_last_name)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verify_the_title_of_the_page() == 'שירות לקוחות'
        assert self.indication_alert(self.indication_message_last_name) == "נא למלא שדה זה"
        self._driver.close()

    @allure.description("Test empty email")
    def test_empty_email_value(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_first_name)
        self.fill_values_to_email_field(self.empty_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verify_the_title_of_the_page() == 'שירות לקוחות'
        assert self.indication_alert(self.indication_message_for_email_xpath) == "נא למלא שדה זה"
        self._driver.close()

    @allure.description("Test empty phone")
    def test_empty_phone_value(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_first_name)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.empty_phone)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verify_the_title_of_the_page() == 'שירות לקוחות'
        assert self.indication_alert(self.indication_message_for_phone_xpath) == "נא למלא שדה זה"
        self._driver.close()

    @allure.description("Test empty referral content")
    def test_empty_content_referral_value(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_first_name)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.empty_referral)
        self.click_on_submit()
        assert self.verify_the_title_of_the_page() == 'שירות לקוחות'
        assert self.indication_alert(self.indication_message_for_content_referral) == "נא למלא שדה זה"
        self._driver.close()

    @allure.description("Test empty first name and last name")
    def test_empty_first_name_and_last_name_value(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.empty_first_name)
        self.fill_values_to_last_name_field(self.empty_last_name)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.empty_referral)
        self.click_on_submit()
        assert self.indication_alert(self.indication_message_for_content_referral) == "נא למלא שדה זה"
        self._driver.close()

    @allure.description("Test empty first name and last name and empty email")
    def test_empty_first_name_and_last_name_value_empty_email(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.empty_first_name)
        self.fill_values_to_last_name_field(self.empty_last_name)
        self.fill_values_to_email_field(self.empty_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.empty_referral)
        self.click_on_submit()
        assert self.indication_alert(self.indication_message_for_content_referral) == "נא למלא שדה זה"

    @allure.description("Test empty first name and empty email")
    def test_empty_first_name_and_empty_email(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.empty_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.empty_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.empty_referral)
        self.click_on_submit()
        assert self.indication_alert(self.indication_message_for_content_referral) == "נא למלא שדה זה"
        self._driver.close()

    @allure.description("Test empty last name and empty email")
    def test_empty_last_name_and_empty_email(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.empty_last_name)
        self.fill_values_to_email_field(self.empty_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.empty_referral)
        self.click_on_submit()
        assert self.indication_alert(self.indication_message_for_content_referral) == "נא למלא שדה זה"
        self._driver.close()

    @allure.description("Test empty last name and empty email and empty phone")
    def test_empty_last_name_and_empty_email_empty_phone(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.empty_last_name)
        self.fill_values_to_email_field(self.empty_email)
        self.fill_values_to_phone_field(self.empty_phone)
        self.fill_values_to_content_field(self.empty_referral)
        self.click_on_submit()
        assert self.indication_alert(self.indication_message_for_content_referral) == "נא למלא שדה זה"
        self._driver.close()

    @allure.description("Test empty email and empty phone")
    def test_empty_email_empty_phone(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.empty_email)
        self.fill_values_to_phone_field(self.empty_phone)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.indication_alert(self.indication_message_for_email_xpath) == "נא למלא שדה זה"
        self._driver.close()

    @allure.description("Test empty email and empty phone and empty last name")
    def test_empty_email_empty_phone_empty_first_name(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.empty_last_name)
        self.fill_values_to_email_field(self.empty_email)
        self.fill_values_to_phone_field(self.empty_phone)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.indication_alert(self.indication_message_for_email_xpath) == "נא למלא שדה זה"
        self._driver.close()

    @allure.description("Test empty phone and empty last name")
    def test_empty_phone_empty_last_name(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.empty_last_name)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.empty_phone)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.indication_alert(self.indication_message_last_name) == "נא למלא שדה זה"
        assert self.indication_alert(self.indication_message_for_phone_xpath) == "נא למלא שדה זה"
        self._driver.close()

    @allure.description("Test empty phone and empty last name")
    def test_empty_phone_empty_last_name(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.empty_last_name)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.empty_phone)
        self.fill_values_to_content_field(self.empty_referral)
        self.click_on_submit()
        assert self.indication_alert(self.indication_message_last_name) == "נא למלא שדה זה"
        assert self.indication_alert(self.indication_message_for_phone_xpath) == "נא למלא שדה זה"
        assert self.indication_alert(self.indication_message_for_content_referral) == "נא למלא שדה זה"
        self._driver.close()

    @allure.description("Test invalid first name")
    def test_all_correct_except_invalid_first_name_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.invalid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.success_message_xpath) == "נא להזין את השם הפרטי הנכון"
        self._driver.close()

    @allure.description("Test invalid last name")
    def test_all_correct_except_invalid_last_name_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.invalid_last_name)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.success_message_xpath) == "נא להזין את השם המשפחה הנכון"
        self._driver.close()

    @allure.description("Test invalid email")
    def test_all_correct_except_invalid_email_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.invalid_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.success_message_xpath) == "נא להזין את האימייל הנכון"
        self._driver.close()

    @allure.description("Test invalid phone")
    def test_all_correct_except_invalid_phone_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.invalid_phone)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description("Test more phone number")
    def test_all_correct_except_more_phone_number_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.more_phone_number)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description("Test less phone number")
    def test_all_correct_except_less_phone_number_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.less_phone_number)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description("Test  phone number with point")
    def test_all_correct_except_phone_number_with_point_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.number_with_point)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description("Test  phone number with text")
    def test_all_correct_except_phone_number_with_text_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.number_text)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description("Test  phone number with text and point")
    def test_all_correct_except_phone_number_with_text_and_point_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.number_text_point)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description("Test  phone number with text and two points")
    def test_all_correct_except_phone_number_with_text_and_two_points_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.number_text_two_pts)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description("Test  phone number with text only")
    def test_all_correct_except_phone_number_with_texts_only_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.only_texts)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description("Test  on phone number field only text and  point")
    def test_all_correct_except_phone_number_with_texts_and_point_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.only_texts_pont)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description("Test  on phone number field only text and two points")
    def test_all_correct_except_phone_number_with_texts_and_two_points_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.only_texts_two_pts)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description("Test  on phone number field numbers in English language text")
    def test_all_correct_except_phone_number_with_in_english_texts_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.texts_num)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description("Test  on phone number field numbers in English language text and comma b/n them")
    def test_all_correct_except_phone_number_with_in_english_texts_with_comma_between_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.comma_bn_num_txt)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description("Test  on phone number field numbers in English language text and dot b/n them")
    def test_all_correct_except_phone_number_with_in_english_texts_with_dot_between_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.txt_num_dot_bn)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description(
        "Test  on phone number field numbers in English language text  and some numeric with one dot b/n them")
    def test_all_correct_except_phone_number_with_in_english_texts_with_and_some_numeric_one_dot_between_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.num_txt_one_dot)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description(
        "Test  on phone number field numbers in English language text  and some numbers with two  dot b/n them")
    def test_all_correct_except_phone_number_with_in_english_texts_and_some_numeric_with_two_dot_between_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(
            self.num_txt_two_dot)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description(
        "Test  on phone number field numbers in English language text and some numeric with out dot b/n them")
    def test_all_correct_except_phone_number_with_in_english_texts_some_numeric_with_out_dot_between_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(
            self.num_txt_no_comma)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description(
        "Test  on phone number field numbers in English language text and some numeric with  comma b/n them")
    def test_all_correct_except_phone_number_with_in_english_texts_some_numeric_with_comma_between_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(
            self.some_num_txt_comma)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description(
        "Test  on phone number field numbers in English language text and some numeric with dot and comma b/n them")
    def test_all_correct_except_phone_number_with_in_english_texts_some_numeric_with_dot_and_comma_between_data(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(
            self.num_txt_comma)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.validation_phone_number) == "מס׳ טלפון לא תקין"
        self._driver.close()

    @allure.description(
        "Test  on phone number field numbers with country code")
    def test_all_correct_except_phone_number_with_country_code(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_last_name_)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(
            self.their_country_code)
        self.fill_values_to_content_field(self.valid_message)
        self.click_on_submit()
        assert self.verifying_success_message(self.success_message_xpath) == "הפרטים נקלטו בהצלחה"
        self._driver.close()

    @allure.description("Test more than 100 words referral content")
    def test_more_than_one_hundred_words_content_referral_value(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_first_name)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.more_than_tabs)
        self.click_on_submit()
        assert self.verify_the_title_of_the_page() == 'שירות לקוחות'
        assert self.verifying_success_message(self.success_message_xpath) == "נא להזין פחות ממאה טבים"
        self._driver.close()

    @allure.description("Test send content referral that has words different languages")
    def test_send_content_referral_that_has_words_different_languages(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_first_name)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.different_lan)
        self.click_on_submit()
        assert self.verify_the_title_of_the_page() == 'שירות לקוחות'
        assert self.verifying_success_message(self.success_message_xpath) == "הפרטים נקלטו בהצלחה"
        self._driver.close()

    @allure.description("Test send content referral in numbers message")
    def test_send_content_referral_in_numbers_message(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_first_name)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.message_numbers)
        self.click_on_submit()
        assert self.verify_the_title_of_the_page() == 'שירות לקוחות'
        assert self.verifying_success_message(self.success_message_xpath) == "הפרטים נקלטו בהצלחה"
        self._driver.close()

    @allure.description("Test send content referral in numbers and text message")
    def test_send_content_referral_in_numbers_and_text_message(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_first_name)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.mege_num_txt)
        self.click_on_submit()
        assert self.verify_the_title_of_the_page() == 'שירות לקוחות'
        assert self.verifying_success_message(self.success_message_xpath) == "הפרטים נקלטו בהצלחה"
        self._driver.close()

    @allure.description("Test send content referral  message with special characters")
    def test_send_content_referral_special_characters_message(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        self.fill_values_to_first_name_field(self.valid_first_name)
        self.fill_values_to_last_name_field(self.valid_first_name)
        self.fill_values_to_email_field(self.valid_email)
        self.fill_values_to_phone_field(self.valid_phone)
        self.fill_values_to_content_field(self.special_char)
        self.click_on_submit()
        assert self.verify_the_title_of_the_page() == 'שירות לקוחות'
        assert self.verifying_success_message(self.success_message_xpath) == "הפרטים נקלטו בהצלחה"
        self._driver.close()

    def test_display_existing_image_on_contact_us(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.images_on_contact_us) == True
        self._driver.close()

    def test_display_active_hours_title_element(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.active_hours_text_title) == True
        self._driver.close()

    @allure.description("Test displaying active hours title")
    def test_display_time_active_hours_element(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.time_active_hours) == True
        self._driver.close()

    @allure.description("Test header color")
    def test_contact_us_header_color(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.color(self.contact_us_header_color) == "rgba(0, 0, 0, 0)"
        self._driver.close()

    @allure.description("Test header text color")
    def test_contact_us_header_text_color(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.color(self.contact_us_header_text) == "rgba(0, 0, 0, 0)"
        self._driver.close()

    @allure.description("Test header text font")
    def test_contact_us_header_text_font(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.checking_font_size(self.contact_us_header_text) == "18px"
        self._driver.close()

    @allure.description("Test on contact us image existanse")
    def test_display_form_image_on_contact_us(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.contact_us_form_image) == True
        self._driver.close()

    @allure.description("Test on contact us footer existence")
    def test_display_footer_existence_on_contact_us(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.contact_us_footer_existence) == True
        self._driver.close()

    @allure.description("Test on contact us footer existence")
    def test_display_footer_existence_on_contact_us(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.contact_us_footer_existence) == True
        self._driver.close()

    @allure.description("Test on contact us place holder existence on firstname field")
    def test_placeholder_for_first_name(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.first_name_xpath) == True
        self._driver.close()

    @allure.description("Verifying the font size of the text placeholder first name")
    def test_placeholder_font_size_for_first_name(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.checking_font_size(self.first_name_xpath) == "16px"
        self._driver.close()

    @allure.description("Verifying the font font weight of the text placeholder first name")
    def test_placeholder_font_weight_for_first_name(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.checking_font_weight(self.first_name_xpath) == "300"
        self._driver.close()

    @allure.description("Test on contact us place holder existence on last name field")
    def test_placeholder_for_last_name(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.last_name_xpath) == True
        self._driver.close()

    @allure.description("Test on contact us place holder existence on email field")
    def test_placeholder_for_email(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.email_xpath) == True
        self._driver.close()

    @allure.description("Test on contact us place holder existence on phone field")
    def test_placeholder_for_phone(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.phone_xpath) == True
        self._driver.close()

    @allure.description("Test on contact us place holder existence on content referral field")
    def test_placeholder_for_content_referral(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.content_referral_xpath) == True
        self._driver.close()

    @allure.description("Test on contact us existence submit button ")
    def test_existence_of_submit_button(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.submit_xpath) == True
        self._driver.close()

    @allure.description("Test on contact us enable submit button ")
    def test_enable_of_submit_button(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self._is_enable(self.submit_xpath) == True
        self._driver.close()

    @allure.description("Test on contact us phone number readable ")
    def test_contact_us_phone_number_readable(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.text_reading(self.contact_us_phone_number_to_connect) == "052-5866695"
        self._driver.close()

    @allure.description("Test on contact us phone number font weight ")
    def test_contact_us_phone_number_font_weight(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.checking_font_weight(self.contact_us_phone_number_to_connect) == "500"
        self._driver.close()

    @allure.description("Test on contact us phone number font size ")
    def test_contact_us_phone_number_font_size(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.checking_font_size(self.contact_us_phone_number_to_connect) == "21.06px"
        self._driver.close()

    @allure.description("Test on contact us is there astrix on first name ")
    def test_astrix_on_first_name(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.text_reading(self.first_name_astrix) == "*"
        self._driver.close()

    @allure.description("Verifying font weight of the astrix  near to first name")
    def test_astrix_on_first_name_font_weight(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.checking_font_weight(self.first_name_astrix) == "600"
        self._driver.close()

    @allure.description("Verifying font color of the astrix  near to first name")
    def test_astrix_on_first_name_font_color(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.color(self.first_name_astrix) == 'rgba(0, 0, 0, 0)'
        self._driver.close()

    @allure.description("Verifying font size of the astrix  near to first name")
    def test_astrix_on_first_name_font_size(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.checking_font_size(self.first_name_astrix) == '14px'
        self._driver.close()

    @allure.description("Verifying if  label  first name is displayed ")
    def test_label_on_first_name_is_displayed(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.first_name_label) == True
        self._driver.close()

    @allure.description("Verifying if  label  first name is is readable ")
    def test_label_on_first_name_is_readable(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.text_reading(self.first_name_label) == "*שם פרטי"
        self._driver.close()

    @allure.description("Verifying font size of the label to first name ")
    def test_label_on_first_name_font_size(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.checking_font_size(self.first_name_label) == '14px'
        self._driver.close()

    @allure.description("Verifying font weight of the label to first name ")
    def test_label_on_first_name_font_weight(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.checking_font_weight(self.first_name_label) == '600'
        self._driver.close()

    @allure.description("Verifying font color of the label to first name ")
    def test_label_on_first_name_font_color(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.color(self.first_name_label) == 'rgba(0, 0, 0, 0)'
        self._driver.close()

    @allure.description("Verifying back_ground color of the contact_us_page ")
    def test_verifying_contact_us_bg_color(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.color(self.contact_us_page_bg_color) == 'rgba(0, 0, 0, 0)'
        self._driver.close()

    @allure.description("Verifying if the contact us form is exist ")
    def test_verifying_contact_us_form_displaying(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.contact_us_form_display) == True
        self._driver.close()

    @allure.description("Verifying if there are images on the contact us right side ")
    def test_verifying_contact_us_form_has_images_on_right_side(self):
        self.handling_the_first_popup()
        self.click_on_contact_us()
        assert self.displaying(self.images_on_right_side_contact_us_form) == True
        self._driver.close()
