from behave import when, then


@when ("I click on the 'Instagram' button")
def step_impl(context):
    context.page.instagram()

@then ("It should redirect to a new browser with the link address 'https://www.instagram.com/edu.gov.ro/'")
def step_impl(context):
    context.page.instagram_validation()

@when ("I click on the 'Facebook' button")
def step_impl(context):
    context.page.facebook()

@then ("It should redirect to a new browser with the link address 'https://www.facebook.com/www.edu.ro/'")
def step_impl(context):
    context.page.facebook_validation()

@when ("I click on the 'Organigramă' button")
def step_impl(context):
    context.page.organigrama()

@then ("It should redirect in the same browser with the link address 'https://www.edu.ro/organigrama'")
def step_impl(context):
    context.page.organigrama_validation()

@when ("I click on the 'Ordine de ministru' button")
def step_impl(context):
    context.page.ordine()

@then ("It should redirect in the same browser with the link address 'https://www.edu.ro/legislațe-ordine-de-ministru'")
def step_impl(context):
    context.page.ordine_validation()