from behave import when, then


@when ("I click on the 'Organigrama' button")
def step_impl(context):
    context.page.organigrama()

@then ("It should redirect in the same browser with the link address 'https://edu.ro/organigrama'")
def step_impl(context):
    context.page.organigrama_validation()

@when ("I click on the 'Harta site-ului' button")
def step_impl(context):
    context.page.harta()

@then ("It should redirect in the same browser with the link address 'https://edu.ro/sitemap'")
def step_impl(context):
    context.page.harta_validation()

@when ("I click on the 'Proiecte acte normative' button")
def step_impl(context):
    context.page.proiecte()

@then ("It should redirect in the same browser with the link address 'https://edu.ro/proiecte-acte-normative'")
def step_impl(context):
    context.page.proiecte_validation()

@when ("I click on the 'Ordine de ministru' button")
def step_impl(context):
    context.page.ordine()

@then ("It should redirect to a new browser with the link address 'https://edu.ro/legislate-ordine-de-ministru'")
def step_impl(context):
    context.page.ordine_validation()