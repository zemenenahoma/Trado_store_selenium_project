import allure
import pytest
from Web.base.BasePage import BasePage
from Web.pages.way_of_sending_page import Way_Of_Sending_page


class Test_Way_Of_Sending(Way_Of_Sending_page, BasePage):

    def handling_the_first_popup(self):
        self.open()
        self.selecting_option_one()
        self.selecting_option_two()
        self.click_save_button()

    @allure.description("Displaying the page How Shipment Works")
    def test_way_of_sending_details(self):
        self.handling_the_first_popup()
        self.click_on_way_of_sending_details()
        assert self.verifying_title() == "שיטת השילוח שלנו נורא פשוטה."
        self._driver.close()

    @allure.description("sending details page header back ground")
    def test_way_of_send_header_bg_color(self):
        self.handling_the_first_popup()
        self.click_on_way_of_sending_details()
        assert self.color(self.background_color_header) == 'rgba(0, 0, 0, 0)'
        self._driver.close()

    @allure.description("sending details page header image")
    def test_image_display(self):
        self.handling_the_first_popup()
        self.click_on_way_of_sending_details()
        assert self.displaying(self.image_on_header) == True
        self._driver.close()

    @allure.description("sending details page body image")
    def test_image_display_on_body(self):
        self.handling_the_first_popup()
        self.click_on_way_of_sending_details()
        assert self.displaying(self.image_on_body) == True
        self._driver.close()

    @allure.description("sending details page footer existance")
    def test_footer_existence(self):
        self.handling_the_first_popup()
        self.click_on_way_of_sending_details()
        assert self.displaying(self.way_of_sending_footer_existanse) == True
        self._driver.close()

    @allure.description("sending details page texts font size")
    def test_way_of_sending_font_text(self):
        self.handling_the_first_popup()
        self.click_on_way_of_sending_details()
        assert self.checking_font_size(self.fonts_way_of_sending_texts) == "23.4px"
        self._driver.close()

    @allure.description("sending details page texts font weight")
    def test_way_of_sending_font_weight_text(self):
        self.handling_the_first_popup()
        self.click_on_way_of_sending_details()
        assert self.checking_font_weight(self.fonts_weight) == '700'
        self._driver.close()

    @allure.description("sending details page texts alignment on the body")
    def test_text_alignment_on_the_header(self):
        self.handling_the_first_popup()
        self.click_on_way_of_sending_details()
        assert self.checking_text_align(self.text_alignment_on_the_body) == 'right'
        self._driver.close()

    @allure.description("sending details page texts alignment on the header")
    def test_text_alignment_header_tittle(self):
        self.handling_the_first_popup()
        self.click_on_way_of_sending_details()
        assert self.checking_text_align(self.page_wa_title_xpath) == 'center'
        self._driver.close()

    @allure.description("sending details page texts reading on the header")
    def test_text_alignment_header_text_reading_tittle(self):
        self.handling_the_first_popup()
        self.click_on_way_of_sending_details()
        self.text_reading(self.page_wa_title_xpath)
        assert self.checking_text_align(self.page_wa_title_xpath) == 'center'
        self._driver.close()

    @allure.description("sending details page  reading texts on the body center")
    def test_text_alignment_header_text_reading_on_body_center(self):
        self.handling_the_first_popup()
        self.click_on_way_of_sending_details()
        self.text_reading(self.text_reading_on_the_body_center)
        assert self.checking_text_align(self.page_wa_title_xpath) == 'center'
        self._driver.close()

    @allure.description("sending details page  reading texts orders and there taxes activity")
    def test_text_alignment_header_text_taxes_activity_hours(self):
        self.handling_the_first_popup()
        self.click_on_way_of_sending_details()
        assert self.text_reading(
            self.orders_and_their_sequence) == 'עלות משטח 160 ש"ח ללא מע"מ   |    זמני הובלה 24-72 שעות   |   ההזמנה מגיעה עד פתח החנות'
        self._driver.close()
