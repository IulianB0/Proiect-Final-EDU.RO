import time

from behave import when, then


@when ("I click on the 'language selector' button")
def step_impl(context):
    context.page.language()

@when ("I click on the 'English' button")
def step_impl(context):
    context.page.language_english()

@then ("It should be visible the 'Engleza' button in Google Translate bar")
def step_impl(context):
    context.page.language_english_validation()