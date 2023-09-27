import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.webdriver import WebDriver


class BasePage(WebDriver):

    def load_url(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))
        return element

    def click(self, xpath):
        locator = (By.XPATH, xpath)
        element = self.wait_for_element(locator)
        element.click()
        self.driver.implicitly_wait(1)

    def click_multiple_times(self, nr, xpath):
        time.sleep(1)
        for _ in range(0, int(nr)):
            self.click(xpath)

    def get_font_size(self, xpath_element):
        locator = (By.XPATH, xpath_element)
        element = self.wait_for_element(locator)
        font_size = element.value_of_css_property("font-size")
        return font_size

    def assert_font_size(self, xpath_element, font_size_to_compare):
        font_size = self.get_font_size(xpath_element)
        assert font_size == font_size_to_compare, f"Font size is {font_size} but expected {font_size_to_compare}"

    def get_text_font_weight(self, xpath_element):
        locator = (By.XPATH, xpath_element)
        element = self.wait_for_element(locator)
        font_weight = element.value_of_css_property("font-weight")
        return font_weight

    def assert_text_font_weight(self, xpath_element, expected_weight):
        text_font_weight = self.get_text_font_weight(xpath_element)
        assert text_font_weight == expected_weight, f"Font-weight-ul textului este {text_font_weight}, dar se aștepta {expected_weight}"

    def get_element_colors(self, xpath_element):
        locator = (By.XPATH, xpath_element)
        element = self.wait_for_element(locator)
        color = element.value_of_css_property("color")
        background = element.value_of_css_property("background-color")
        return color, background


    def assert_colors(self, xpath_element, expected_color, expected_background):
        color, background = self.get_element_colors(xpath_element)
        assert color == expected_color, f"Text color is {color} but expected {expected_color}"
        assert background == expected_background, f"Background color is {background}, but expected {expected_background}"

    def get_current_url(self):
        time.sleep(1)
        current_url = self.driver.current_url
        return current_url

    def assert_url(self, expected_url):
        current_url = self.get_current_url()
        assert current_url == expected_url, f"Current URL '{current_url}' does not match expected URL '{expected_url}'"

    def hover_over(self, xpath):
        locator = (By.XPATH, xpath)
        element = self.wait_for_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def assert_text(self, xpath_text, expected_text):
        locator = (By.XPATH, xpath_text)
        element = self.wait_for_element(locator)
        actual_text = element.text
        assert actual_text == expected_text, f"Current text '{actual_text}' does not match expected text '{expected_text}"

    def fill_text(self, text, text_xpath):
        locator = (By.XPATH, text_xpath)
        element = self.wait_for_element(locator)
        element.send_keys(text)

    def press_enter(self, xpath):
        locator = (By.XPATH, xpath)
        element = self.wait_for_element(locator)
        element.send_keys(Keys.ENTER)

    def clear_text(self, xpath):
        locator = (By.XPATH, xpath)
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].value = '';", element)

    def click_link_and_switch_to_new_window(self, xpath_element):
        current_window_handle = self.driver.current_window_handle
        self.click(xpath_element)
        self.wait_for_new_window(current_window_handle)

    def wait_for_new_window(self, old_window_handle):
        new_window_handle = self.get_new_window_handle(old_window_handle)
        self.driver.switch_to.window(new_window_handle)

    def get_new_window_handle(self, old_window_handle):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != old_window_handle:
                return handle
