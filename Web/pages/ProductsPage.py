import allure
from selenium import webdriver
from selenium.webdriver.common.actions.interaction import KEY

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from Web.base.BasePage import BasePage
from Web.data.data import Data
from Web.locators.ProductsLocators import AdminProductsLocators


class ProductPage(BasePage, AdminProductsLocators, Data):

    def verify_the_title_of_the_page(self, page):
        return self._find(page).text

    def displaying(self, display):
        return self._is_displayed(display)

    def verifying_success_message(self, success_message):
        return self._find(success_message).text

    def fill_phone_code(self, phone):
        self._entry(self.phone_code, phone)

    def click_on_submit(self):
        self._click(self.form_submit_button)

    def fill_admin_code(self, code_admin):
        self._entry(self.phone_code, code_admin)

    def fill_bar_code(self, bar_codes):
        self._entry(self.bar_code, bar_codes)

    def fill_product_name(self, product):
        self._entry(self.product_name, product)

    def fill_price(self, prices):
        self._entry(self.price, prices)

    def fill_date(self, dates):
        self._entry(self.date, dates)

    def fill_description(self, descriptions):
        self._entry(self.description, descriptions)

    def remember_click_on(self):
        self._click(self.remember_click)

    def click_on_next(self):
        self._click(self.next_button)

    def click_on_login(self):
        self._click(self.form_login)

    def click_on_products(self, click):
        self._click(click)

    def click_on_product1(self, click):
        self._click(click)

    def selection_click(self, sectionId):
        self._click(sectionId)

    def selection_send(self, section_id, content):
        self._entry(section_id, content)

    def click_on_selection(self, selection):
        self._click(selection)

    def click_on_add(self, add):
        self._click(add)

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
