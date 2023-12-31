import time

from pages.base_page import BasePage
from pages.page_objects import PageObjects


class HomePage(BasePage, PageObjects):

    def home_page(self):
        self.load_url(PageObjects.home_url)

    def home_page_first_time(self):
        try:
            self.click(PageObjects.popup_xpath_button)
        except:
            pass

    def click_accessibility(self):
        self.click(PageObjects.accessibility_xpath_button)
        time.sleep(2)

    def click_increase(self):
        time.sleep(1)
        self.click_multiple_times(16, (PageObjects.accessibility_increase_size_xpath_button))

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
        time.sleep(2)
        self.click(PageObjects.accessibility_page_style_xpath_button)

    def page_style_black_white(self):
        time.sleep(2)
        self.click(PageObjects.accessibility_black_white_page_style_xpath_button)

    def page_style_black_white_validation(self):
        time.sleep(1)
        self.get_and_assert_colors(PageObjects.language_comunicate_xpath_text, "rgba(0, 0, 0, 1)", "rgba(255, 255, 255, 1)")

    def page_style_white_black(self):
        time.sleep(2)
        self.click(PageObjects.accessibility_white_black_page_style_xpath_button)

    def page_style_white_black_validation(self):
        time.sleep(1)
        self.get_and_assert_colors(PageObjects.language_noutati_xpath_text, "rgba(255, 255, 255, 1)", "rgba(255, 255, 255, 1)")

    def page_style_yellow_blue(self):
        time.sleep(2)
        self.click(PageObjects.accessibility_yellow_blue_page_style_xpath_button)

    def page_style_yellow_blue_validation(self):
        time.sleep(1)
        self.get_and_assert_colors(PageObjects.language_legile_xpath_text, "rgba(255, 255, 0, 1)", "rgba(0, 0, 255, 1)")

    def page_style_standard(self):
        time.sleep(2)
        self.click(PageObjects.accessibility_standard_page_style_xpath_button)

    def page_style_standard_validation(self):
        self.get_and_assert_colors(PageObjects.language_proiecte_xpath_text, "rgba(51, 51, 51, 1)", "rgba(0, 0, 0, 0)")

    def organigrama(self):
        self.click(PageObjects.footer_organigrama_xpath_button)
        time.sleep(2)

    def organigrama_validation(self):
        self.get_and_assert_url(PageObjects.organigrama_url)

    def harta(self):
        self.click(PageObjects.footer_harta_xpath_button)

    def harta_validation(self):
        self.get_and_assert_url(PageObjects.harta_url)

    def proiecte(self):
        self.click(PageObjects.footer_proiecte_xpath_button)

    def proiecte_validation(self):
        self.get_and_assert_url(PageObjects.proiecte_url)

    def ordine(self):
        self.click_link_and_switch_to_new_window(PageObjects.footer_oridine_xpath_button)

    def ordine_validation(self):
        self.get_and_assert_url(PageObjects.ordine_url)

    def contact_page(self):
        self.load_url(PageObjects.contact_url)

    def logo(self):
        self.click(PageObjects.header_logo_image_xpath_button)

    def home_page_validation(self):
        self.get_and_assert_url(PageObjects.home_url)

    def hover_minister(self):
        self.click(PageObjects.header_minister_xpath_button)
        time.sleep(2)

    def minister_validation(self):
        self.assert_text(PageObjects.header_contact_xpath_text, PageObjects.header_contact_text)

    def hover_invatamant_primar(self):
        self.click(PageObjects.header_invatamant_preuniversitar_xpath_button)
        time.sleep(2)

    def invatamant_primar_validation(self):
        self.assert_text(PageObjects.header_invatamant_primar_xpath_text, PageObjects.header_invatamant_primar_text)

    def hover_invatamant_superior(self):
        self.click(PageObjects.header_invatamant_superior_xpath_button)
        time.sleep(2)

    def invatamant_superior_validation(self):
        self.assert_text(PageObjects.header_studii_universitare_xpath_text, PageObjects.header_studii_universitare_text)

    def hover_romania(self):
        self.click(PageObjects.header_romania_xpath_button)
        time.sleep(2)

    def romania_validation(self):
        self.assert_text(PageObjects.header_memorandul_xpath_text, PageObjects.header_memorandul_text)

    def hover_cooperare(self):
        self.click(PageObjects.header_cooperare_xpath_button)
        time.sleep(2)

    def cooperare_validation(self):
        self.assert_text(PageObjects.header_studiaza_xpath_text,PageObjects.header_studiaza_text)

    def search_studii(self):
        self.fill_text(PageObjects.search_studii_text, PageObjects.search_menu_xpath_form)

    def press_enter_key(self):
        self.press_enter(PageObjects.search_menu_xpath_form)

    def first_result_studii(self):
        self.assert_text(PageObjects.search_result_xpath_text, PageObjects.search_studii_text)

    def clear_form(self):
        self.clear_text(PageObjects.search_bar_xpath_form)

    def search_invatamant(self):
        time.sleep(1)
        self.fill_text(PageObjects.search_bacalaurea_text, PageObjects.search_bar_xpath_form)

    def search(self):
        self.click(PageObjects.search_xpath_button)
        time.sleep(1)

    def first_result_invatamant(self):
        self.assert_text(PageObjects.search_result_xpath_text, PageObjects.search_bacalaurea_text)

    def search_valid(self):
        self.fill_text(PageObjects.search_valid_class_text, PageObjects.search_menu_xpath_form)

    def search_validation(self):
        self.assert_text(PageObjects.search_cautare_xpath_text, PageObjects.search_cautare_text)

    def search_valid_bar(self):
        self.fill_text(PageObjects.search_valid_class_text, PageObjects.search_bar_xpath_form)

    def search_error(self):
        self.assert_text(PageObjects.search_error_xpath, PageObjects.search_error_va_rugam_message)

    def search_page(self):
        self.load_url(PageObjects.search_url)

    def search_invalid_bar(self, special_caracters):
        self.fill_text(special_caracters, PageObjects.search_bar_xpath_form)

    def search_2_error(self):
        self.assert_text(PageObjects.search_error_xpath, PageObjects.search_error_you_must_message)

    def language(self):
        self.click(PageObjects.language_xpath_button)
        time.sleep(1)

    def language_english(self):
        self.click(PageObjects.language_english_xpath_button)
        time.sleep(1)

    def language_english_validation(self):
        time.sleep(2)
        self.assert_text(PageObjects.language_comunicate_xpath_text, PageObjects.language_comunicate_english_text)
