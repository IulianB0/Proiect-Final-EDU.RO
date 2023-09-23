import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utils.webdriver import WebDriver


class BasePage(WebDriver):

    def load_url(self, url):
        self.driver.get(url)

    def click(self, xpath_button):
        self.driver.find_element(By.XPATH, xpath_button).click()
        self.driver.implicitly_wait(1)

    # def click_id(self, id_button):
    #     self.driver.find_element(By.ID, id_button).click()
    #     self.driver.implicitly_wait(1)

    def fill_text(self, text, text_xpath):
        self.driver.find_element(By.XPATH, text_xpath).send_keys(text)
        self.driver.implicitly_wait(1)

    def click_multiple_times(self, nr, xpath_button):
        time.sleep(1)
        for _ in range(0, int(nr)):
            self.click(xpath_button)

    def get_font_size(self, xpath_adress):
        adress = self.driver.find_element(By.XPATH, xpath_adress)
        font_size = adress.value_of_css_property("font-size")
        return font_size

    def assert_font_size(self, xpath_element, font_size_to_compare):
        font_size = self.get_font_size(xpath_element)
        assert font_size == font_size_to_compare, f"Font size is {font_size} but expected {font_size_to_compare}"

    def get_text_font_weight(self, xpath_element):
        weight = self.driver.find_element(By.XPATH, xpath_element)
        font_weight = weight.value_of_css_property("font-weight")
        return font_weight

    def assert_text_font_weight(self, xpath_element, expected_weight):
        text_font_weight = self.get_text_font_weight(xpath_element)
        assert text_font_weight == expected_weight, f"Font-weight-ul textului este {text_font_weight}, dar se aștepta {expected_weight}"

    def get_element_colors(self, xpath_element):
        element = self.driver.find_element(By.XPATH, xpath_element)
        color = element.value_of_css_property("color")
        background = element.value_of_css_property("background-color")
        return color, background

    def assert_colors(self, xpath_element, expected_color, expected_background):
        color, background = self.get_element_colors(xpath_element)
        assert color == expected_color, f"Text color is {color} but expected {expected_color}"
        assert background == expected_background, f"Background color is {background}, but expected {expected_background}"

    def get_current_url(self):
        self.driver.implicitly_wait(3)
        current_url = self.driver.current_url
        return current_url

    def assert_url(self, expected_url):
        current_url = self.get_current_url()
        assert current_url == expected_url, f"Current URL '{current_url}' does not match expected URL '{expected_url}'"

    def hover_over(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def assert_text(self, xpath_text, expected_text):
        xpath = self.driver.find_element(By.XPATH, xpath_text)
        actual_text = xpath.text
        assert actual_text == expected_text, , f"Current text '{actual_text}' does not match expected text '{expected_text}"