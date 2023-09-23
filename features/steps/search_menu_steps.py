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

@when ("I replaces in the search bar 'Studii universitare de master' with the text 'Învățământ primar'")
def step_impl(context):
    context.page.clear_form()
    context.page.search_invatamant()

@when ("I press the 'Căutare' button")
def step_impl(context):
    context.page.search()

@then ("It should be visible and the first result should be identical to text 'Învățământ primar'")
def step_impl(context):
    context.page.first_result_invatamant()

@when  ("I enter the text '   '(3 blank spaces) in the search menu")
def step_impl(context):
    context.page.search_valid()

@then ("It should be visible the message 'Căutare'")
def step_impl(context):
    context.page.search_validation()

@when ("I enter the text '   '(3 blank spaces) in the search bar")
def step_impl(context):
    context.page.search_valid_bar()


@then ("It should be visible the error message 'Vă rugăm să introduceți câteva cuvinte cheie.'")
def step_impl(context):
    context.page.search_error()

@when  ("I enter the text '///' in the search menu")
def step_impl(context):
    context.page.search_invalid()

@when ("I enter the text '///' in the search bar")
def step_impl(context):
    context.page.search_invalid_bar()