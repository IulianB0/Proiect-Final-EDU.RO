from behave import given, when, then


@given ("I am on the contact page")
def step_impl(context):
    context.page.contact_page()

@when ("I click on the 'Logo' image")
def step_impl(context):
    context.page.logo()

@then ("It should be redirected to the home page")
def step_impl(context):
    context.page.home_page_validation()

@when ("I hold the mouse over the 'Minister' button")
def step_impl(context):
    context.page.hover_minister()

@then ("It should be visible the text 'Date de contact'")
def step_impl(context):
    context.page.minister_validation()


@when ("I hold the mouse over the 'Invatamant preuniversitar' button")
def step_impl(context):
    context.page.hover_invatamant_primar()

@then ("It should be visible the text 'Invatamant primar'")
def step_impl(context):
    context.page.invatamant_primar_validation()

@when ("I hold the mouse over the 'Invatamant superior' button")
def step_impl(context):
    context.page.hover_invatamant_superior()

@then ("It should be visible the text 'Studii universitare de licenta'")
def step_impl(context):
    context.page.invatamant_superior_validation()

@when ("I hold the mouse over the 'Romania educata' button")
def step_impl(context):
    context.page.hover_romania()

@then ("It should be visible the text 'Memorandum implementare'")
def step_impl(context):
    context.page.romania_validation()

@when ("I hold the mouse over the 'Cooperare internationala' button")
def step_impl(context):
    context.page.hover_cooperare()

@then ("It should be visible the text 'Studiaza in Romania'")
def step_impl(context):
    context.page.cooperare_validation()