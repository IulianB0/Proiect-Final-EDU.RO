from behave import when, then


@when ("I enter the text 'Studii universitare de master' in the search menu")
def step_impl(context):
    context.page.search_studii()

@when ("I press the 'ENTER' button on the keyboard")
def step_impl(context):
    context.page.press_enter_key()

@then ("It should be visible and the first result should be identical to text 'Studii universitare de master'")
def step_impl(context):
    context.page.first_result_studii()

@when ("I replaces in the search bar 'Studii universitare de master' with the text 'Bacalaurea'")
def step_impl(context):
    context.page.clear_form()
    context.page.search_invatamant()

@when ("I press the 'Cautare' button")
def step_impl(context):
    context.page.search()

@then ("It should be visible and the first result should be identical to text 'Bacalaureat'")
def step_impl(context):
    context.page.first_result_invatamant()

@when  ("I enter the text '   '(3 blank spaces) in the search menu")
def step_impl(context):
    context.page.search_valid()

@then ("It should be visible the message 'Cautare'")
def step_impl(context):
    context.page.search_validation()

@when ("I enter the text '   '(3 blank spaces) in the search bar")
def step_impl(context):
    context.page.search_valid_bar()


@then ("It should be visible the error message 'Va rugam sa introduceti cateva cuvinte cheie.'")
def step_impl(context):
    context.page.search_error()


@given ("I am on the search page")
def step_impl(context):
    context.page.search_page()

@when ("I enter '{special_caracters}' in the search bar")
def step_impl(context, special_caracters):
    context.page.search_invalid_bar(special_caracters)

@then ("It should be visible the error message 'You must include at least one positive keyword with 3 characters or more.'")
def step_impl(context):
    context.page.search_2_error()