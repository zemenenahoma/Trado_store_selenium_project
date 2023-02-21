from Web.base.BasePage import BasePage
from Web.data.data import Data
from Web.locators.way_of_sending_locators import Way_Of_Sending_Locators


class Way_Of_Sending_page(BasePage, Way_Of_Sending_Locators, Data):

    def selecting_option_one(self):
        self._click(self.option1)

    def selecting_option_two(self):
        self._click(self.option2)

    def click_save_button(self):
        self._click(self.save)

    def displaying(self, display):
        return self._is_displayed(display)

    def click_on_way_of_sending_details(self):
        self._click(self.more_details)

    def verifying_title(self):
        return self._find(self.page_wa_title_xpath).text

    def color(self, location):
        element_color = self._find(location).value_of_css_property("background-color")
        return element_color

    def checking_font_size(self, location):
        return self._find(location).value_of_css_property("font-size")

    def checking_font_weight(self, location):
        return self._find(location).value_of_css_property("font-weight")

    def checking_text_align(self, location):
        return self._find(location).value_of_css_property("text-align")
