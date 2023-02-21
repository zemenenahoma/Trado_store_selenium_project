import allure
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from Web.data.data import Data


class BasePage(Data):
    _driver = webdriver.Chrome()

    def _find(self, locate) -> WebElement:
        self._wait_until_element_is_visible(locate)
        return self._driver.find_element(*locate)

    def _entry(self, locate, content):
        self._wait_until_element_is_visible(locate)
        self._find(locate).send_keys(content)

    def _wait_until_element_is_visible(self, locate, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locate))

    def scroll(self, locate, up_to):
        self._wait_until_element_is_visible(locate)
        self._driver.execute_script(up_to)

    def _click(self, locate):
        self._wait_until_element_is_visible(locate)
        self._find(locate).click()

    def _is_displayed(self, locate) -> bool:
        return self._find(locate).is_displayed()

    def _is_enable(self, locate) -> bool:
        return self._find(locate).is_enabled()

    def _find_elements(self, locator):
        self._wait_until_element_is_visible(locator)
        return self._driver.find_elements(*locator)

    @allure.step("Opening the website")
    def open(self):
        self._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self._driver.get(self.url)
        self._driver.maximize_window()

    def open_admin(self):
        _driver = webdriver.Chrome()
        self._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self._driver.get(self.url_admin)
        self._driver.maximize_window()

    def text_reading(self, locate):
        return self._find(locate).text
