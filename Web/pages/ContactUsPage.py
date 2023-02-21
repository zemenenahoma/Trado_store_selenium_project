from Web.base.BasePage import BasePage
from Web.data.data import Data
from Web.locators.ContactUsLocators import ContactUsLocators


class ContactUsPage(BasePage, ContactUsLocators, Data):

    def selecting_option_one(self):
        self._click(self.option1)

    def selecting_option_two(self):
        self._click(self.option2)

    def click_save_button(self):
        self._click(self.save)

    def click_on_contact_us(self):
        self._click(self.contact_us_xpath)

    def verify_the_title_of_the_page(self):
        return self._find(self.page_title).text

    def displaying(self, display):
        return self._is_displayed(display)

    def verifying_success_message(self, success_message):
        return self._find(success_message).text

    def fill_values_to_first_name_field(self, name):
        self._entry(self.first_name_xpath, name)

    def fill_values_to_last_name_field(self, last_name):
        self._entry(self.last_name_xpath, last_name)

    def fill_values_to_email_field(self, email):
        self._entry(self.email_xpath, email)

    def fill_values_to_phone_field(self, phone):
        self._entry(self.phone_xpath, phone)

    def fill_values_to_content_field(self, message):
        self._entry(self.content_referral_xpath, message)

    def click_on_submit(self):
        self._click(self.submit_xpath)

    def indication_alert(self, indication):
        return self._find(indication).text

    def color(self, location):
        element_color = self._find(location).value_of_css_property("background-color")
        return element_color

    def checking_font_size(self, location):
        return self._find(location).value_of_css_property("font-size")

    def checking_font_weight(self, location):
        return self._find(location).value_of_css_property("font-weight")

    def checking_text_align(self, location):
        return self._find(location).value_of_css_property("text-align")
