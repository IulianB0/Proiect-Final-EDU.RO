class PageObjects():
# links
    home_url = "https://edu.ro/"
    contact_url = "https://edu.ro/contact"
    harta_url = "https://edu.ro/sitemap"
    proiecte_url = "https://edu.ro/proiecte-acte-normative"
    organigrama_url = "https://www.edu.ro/organigrama"
    ordine_url = "https://www.edu.ro/legisla%C8%9Bie-ordine-de-ministru"
    search_url = "https://www.edu.ro/search/node/"
# buttons
    popup_xpath_button = "//div[@id='popup-buttons']/button[1]"
    accessibility_xpath_button = "//div[@class='help-bttn']"
    accessibility_increase_size_xpath_button = "//img[@alt='Increase']"
    accessibility_decrease_size_xpath_button = "//img[@alt='Decrease']"
    accessibility_normal_size_xpath_button = "//img[@alt='Normal']"
    accessibility_ridicat_contrast_xpath_button = "//span[@class='high_contrast_switcher_high']/a"
    accessibility_normal_contrast_xpath_button = "//span[@class='high_contrast_switcher_normal']/a"
    accessibility_page_style_xpath_button = "//*[@id='edit-pagestyle-select']"
    accessibility_black_white_page_style_xpath_button = "//*[@id='edit-pagestyle-select']/option[1]"
    accessibility_white_black_page_style_xpath_button = "//*[@id='edit-pagestyle-select']/option[2]"
    accessibility_yellow_blue_page_style_xpath_button = "//*[@id='edit-pagestyle-select']/option[3]"
    accessibility_standard_page_style_xpath_button = "//select[@id='edit-pagestyle-select']/option[4]"
    footer_proiecte_xpath_button = "//*[@id='block-block-6']/ul/li[1]/p/a"
    footer_harta_xpath_button = "//*[@id='block-block-4']/ul/li[4]/p/a"
    footer_organigrama_xpath_button = "//div[@id='block-block-4']/ul/li[1]/p/a"
    footer_oridine_xpath_button = "//div[@id='block-block-4']/ul/li[2]/p/a"
    header_logo_image_xpath_button = "//*[@id='logo-image']"
    header_minister_xpath_button = "//div[@id='tb-megamenu-main-menu']/div/ul/li[1]"
    header_invatamant_preuniversitar_xpath_button = "//div[@id='tb-megamenu-main-menu']/div/ul/li[2]"
    header_invatamant_superior_xpath_button = "//div[@id='tb-megamenu-main-menu']/div/ul/li[3]"
    header_romania_xpath_button = "//div[@id='tb-megamenu-main-menu']/div/ul/li[4]"
    header_cooperare_xpath_button = "//div[@id='tb-megamenu-main-menu']/div/ul/li[5]"
    header_contact_xpath_text = "//*[@id='tb-megamenu-column-1']/div/ul/li[1]/a"
    header_invatamant_primar_xpath_text = "//*[@id='tb-megamenu-column-6']/div/ul/li[4]/a"
    header_studii_universitare_xpath_text = "//*[@id='tb-megamenu-column-8']/div/ul/li[2]/a"
    header_memorandul_xpath_text = "//*[@id='tb-megamenu-column-10']/div/ul/li[1]/a"
    header_studiaza_xpath_text = "//*[@id='tb-megamenu-column-11']/div/ul/li[2]/a"
    language_xpath_button = "//span[@class='select2-selection__arrow' and @role='presentation']"
    language_english_xpath_button = "//*[@id='search-language-column']/span/span/span[2]/ul/li[4]"
    search_xpath_button = "//input[@id='edit-submit']"
    search_error_xpath = "//*[@id='main']/div[2]/div/div[1]"
# text
    header_contact_text = "Date de contact"
    header_invatamant_primar_text = "Învățământ primar"
    header_studii_universitare_text = "Studii universitare de licență"
    header_memorandul_text = "Memorandum implementare"
    header_studiaza_text = "Studiază în România"
    language_comunicate_text = "Comunicate de presă"
    language_comunicate_english_text = "Press Releases"
    search_studii_text = "Studii universitare de master"
    search_bacalaurea_text = "Bacalaurea"
    search_valid_class_text = "   "
    search_cautare_text = "Căutare"
# location text
    language_comunicate_xpath_text = "//*[@id='block-views-comunicate-de-presa-block-1']/h2"
    language_noutati_xpath_text = "//*[@id='block-views-noutati-block']/h2"
    language_legile_xpath_text = "//*[@id='block-menu-menu-diaspora']/ul/li[1]/a"
    language_proiecte_xpath_text = "//*[@id='block-menu-menu-dezbatere-publica']/ul/li[1]/a"

    search_result_xpath_text = "//*[@id='content']/div/ol/li[1]/h3/a"
    search_cautare_xpath_text = "//*[@id='page-title']"
# forms
    language_xpath_form = "//span[@id='select2-c14v-container']/div"
    search_menu_xpath_form = "//input[@id='edit-search-block-form--2']"
    search_bar_xpath_form = "//input[@id='edit-keys']"
# messages
    search_error_va_rugam_message = "Vă rugăm să introduceţi câteva cuvinte cheie."
    search_error_you_must_message = "You must include at least one positive keyword with 3 characters or more."