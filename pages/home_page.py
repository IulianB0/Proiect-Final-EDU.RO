import time

from pages.base_page import BasePage
from pages.page_objects import PageObjects


class HomePage(BasePage, PageObjects):

    def home_page(self):
        self.load_url(PageObjects.home_url)

    def click_accessibility(self):
        self.click(PageObjects.accessibility_xpath_button)

    def click_increase(self):
        self.click_multiple_times(16, (PageObjects.accessibility_increase_size_xpath_button))
        time.sleep(2)

    def font_increases_validation(self):
        self.assert_font_size(PageObjects.language_comunicate_xpath_text, "30px")

    def click_normal_size(self):
        self.click((super().accessibility_normal_size_xpath_button))

    def font_validation(self):
        self.assert_font_size(PageObjects.language_comunicate_xpath_text, "30px")

    def click_decrease(self):
        self.click_multiple_times(8, PageObjects.accessibility_decrease_size_xpath_button)
        time.sleep(2)

    def font_decreases_validation(self):
        self.assert_font_size(PageObjects.language_comunicate_xpath_text, "30px")

    def contrast_ridicat(self):
        self.click(PageObjects.accessibility_ridicat_contrast_xpath_button)

    def contrast_ridicat_validation(self):
        self.assert_text_font_weight(PageObjects.language_comunicate_xpath_text, 300)

    def contrast_normal(self):
        self.click(PageObjects.accessibility_normal_contrast_xpath_button)

    def contrast_normal_validation(self):
        self.assert_text_font_weight(PageObjects.language_comunicate_xpath_text, 300)

    def page_style(self):
        self.click(PageObjects.accessibility_page_style_xpath_button)

    def page_style_black_white(self):
        self.click(PageObjects.accessibility_black_white_page_style_xpath_button)

    def page_style_black_white_validation(self):
        self.assert_colors(PageObjects.language_comunicate_xpath_text, "rgba(51, 51, 51, 1)", "rgba(0, 0, 0, 0)")

    def page_style_white_black(self):
        self.click(PageObjects.accessibility_white_black_page_style_xpath_button)

    def page_style_white_black_validation(self):
        self.assert_colors(PageObjects.language_comunicate_xpath_text, "rgba(51, 51, 51, 1)", "rgba(0, 0, 0, 0)")

    def page_style_yellow_blue(self):
        self.click(PageObjects.accessibility_yellow_blue_page_style_xpath_button)

    def page_style_yellow_blue_validation(self):
        self.assert_colors(PageObjects.language_comunicate_xpath_text, "rgba(51, 51, 51, 1)", "rgba(0, 0, 0, 0)")

    def page_style_standard(self):
        self.click(PageObjects.accessibility_standard_page_style_xpath_button)

    def page_style_standard_validation(self):
        self.assert_colors(PageObjects.language_comunicate_xpath_text, "rgba(51, 51, 51, 1)", "rgba(0, 0, 0, 0)")

    def instagram(self):
        self.click_link_and_switch_to_new_window(PageObjects.footer_instagram_xpath_button)


    def instagram_validation(self):
        self.assert_url(PageObjects.instagram_url)

    def facebook(self):
        self.click_link_and_switch_to_new_window(PageObjects.footer_facebook_xpath_button)


    def facebook_validation(self):
        self.assert_url(PageObjects.facebook_url)

    def organigrama(self):
        self.click(PageObjects.footer_organigrama_xpath_button)


    def organigrama_validation(self):
        self.assert_url(PageObjects.organigrama_url)

    def ordine(self):
        self.click_link_and_switch_to_new_window(PageObjects.footer_oridine_xpath_button)


    def ordine_validation(self):
        self.assert_url(PageObjects.ordine_url)

    def contact_page(self):
        self.load_url(PageObjects.contact_url)

    def logo(self):
        self.click(PageObjects.header_logo_image_xpath_button)

    def home_page_validation(self):
        self.assert_url(PageObjects.home_url)

    def hover_minister(self):
        self.hover_over(PageObjects.header_minister_xpath_button)

    def minister_validation(self):
        self.assert_text(PageObjects.header_contact_xpath_text, PageObjects.header_contact_text)

    def hover_invatamant_primar(self):
        self.hover_over(PageObjects.header_invatamant_preuniversitar_xpath_button)

    def invatamant_primar_validation(self):
        self.assert_text(PageObjects.header_invatamant_primar_xpath_text, PageObjects.header_invatamant_primar_text)

    def hover_invatamant_superior(self):
        self.hover_over(PageObjects.header_invatamant_superior_xpath_button)

    def invatamant_superior_validation(self):
        self.assert_text(PageObjects.header_studii_universitare_xpath_text, PageObjects.header_studii_universitare_text)

    def hover_romania(self):
        self.hover_over(PageObjects.header_romania_xpath_button)

    def romania_validation(self):
        self.assert_text(PageObjects.header_memorandul_xpath_text, PageObjects.header_memorandul_text)

    def hover_cooperare(self):
        self.hover_over(PageObjects.header_cooperare_xpath_button)

    def cooperare_validation(self):
        self.assert_text(PageObjects.header_studiaza_xpath_text,PageObjects.header_studiaza_text)

    def language(self):
        self.click(PageObjects.language_xpath_button)

    def language_english(self):
        self.click(PageObjects.language_english_xpath_button)

    def language_english_validation(self):
        self.assert_text(PageObjects.language_google_xpath_button, PageObjects.language_google_engleza_text)

    def language_google(self):
        self.click(PageObjects.language_google_xpath_button)

    def language_bulgara(self):
        self.click(PageObjects.language_google_bulgara_xpath_button)

    def language_bulgara_validation(self):
        self.assert_text(PageObjects.language_google_xpath_button, PageObjects.language_google_bulgara_text)

    def language_close(self):
        self.click(PageObjects.language_google_close_xpath_button)

    def language_validation(self):
        self.assert_text(PageObjects.language_comunicate_xpath_text, PageObjects.language_comunicate_text)

    def search_studii(self):
        self.fill_text(PageObjects.search_studii_text, PageObjects.search_menu_xpath_form)

    def press_enter_key(self):
        self.press_enter(PageObjects.search_menu_xpath_form)

    def first_result_studii(self):
        self.assert_text(PageObjects.search_result_xpath_text, PageObjects.search_studii_text)

    def clear_form(self):
        self.clear_text(PageObjects.search_bar_xpath_form)

    def search_invatamant(self):
        self.fill_text(PageObjects.search_invatamant_text, PageObjects.search_bar_xpath_form)

    def search(self):
        self.click(PageObjects.search_xpath_button)

    def first_result_invatamant(self):
        self.assert_text(PageObjects.search_result_xpath_text, PageObjects.search_invatamant_text)

    def search_valid(self):
        self.fill_text(PageObjects.search_valid_class_text, PageObjects.search_menu_xpath_form)

    def search_validation(self):
        self.assert_text(PageObjects.search_cautare_xpath_text, PageObjects.search_cautare_text)

    def search_valid_bar(self):
        self.fill_text(PageObjects.search_valid_class_text, PageObjects.search_bar_xpath_form)

    def search_error(self):
        self.assert_text(PageObjects.search_error_message, PageObjects.search_error_xpath)

    def search_invalid(self):
        self.fill_text(PageObjects.search_invalid_class_text, PageObjects.search_menu_xpath_form)

    def search_invalid_bar(self):
        self.fill_text(PageObjects.search_invalid_class_text, PageObjects.search_bar_xpath_form)