from behave import when, then


@when ("I click on the 'language selector' button")
def step_impl(context):
    context.page.language()

@when ("I click on the 'English' button")
def step_impl(context):
    context.page.language_english()

@then ("It should be visible the 'Engleză' button in Google Translate bar")
def step_impl(context):
    context.page.language_english_validation()

@when ("I click on the 'Engleză' button from the Google Translate bar")
def step_impl(context):
    context.page.language_google()

@when ("I click on the 'Bulgară' button from the Google Translate bar")
def step_impl(context):
    context.page.language_bulgara()

@then ("It should be visible the 'Bulgară' button in Google Translate bar")
def step_impl(context):
    context.page.language_bulgara_validation()

@when ("I click on the 'close' button from the Google Translate bar")
def step_impl(context):
    context.page.language_close()

@then ("It should be visible that the text returns to the Romanian language")
def step_impl(context):
    context.page.language_validation()