from behave import when, then


@when ("I click on the 'Instagram' button")
def step_impl(context):
    context.page.instagram()

@then ("It should redirect to a new browser with the link address 'https://instagram.com/edu.gov.ro/'")
def step_impl(context):
    context.page.instagram_validation()

@when ("I click on the 'Facebook' button")
def step_impl(context):
    context.page.facebook()

@then ("It should redirect to a new browser with the link address 'https://facebook.com/www.edu.ro/'")
def step_impl(context):
    context.page.facebook_validation()

@when ("I click on the 'Organigrama' button")
def step_impl(context):
    context.page.organigrama()

@then ("It should redirect in the same browser with the link address 'https://edu.ro/organigrama'")
def step_impl(context):
    context.page.organigrama_validation()

@when ("I click on the 'Ordine de ministru' button")
def step_impl(context):
    context.page.ordine()

@then ("It should redirect to a new browser with the link address 'https://edu.ro/legislate-ordine-de-ministru'")
def step_impl(context):
    context.page.ordine_validation()