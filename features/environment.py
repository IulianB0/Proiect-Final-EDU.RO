from pages.home_page import HomePage
from utils.webdriver import WebDriver


def before_all(context):
    context.webdriver = WebDriver()
    context.page = HomePage()

def after_all(context):
    context.webdriver.quit()
