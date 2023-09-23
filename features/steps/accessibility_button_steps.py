from behave import given, when, then


@given ("I am on the home page")
def step_impl(context):
    context.page.home_page()

@when ("I click on the 'Accessibility' button")
def step_impl(context):
    context.page.click_accessibility()

@when ("I click on the '+' button 16 times")
def step_impl(context):
    context.page.click_increase()

@then ("It should be visible that the text in the page increases its size")
def step_impl(context):
    context.page.font_increases_validation()

@when ("I click on the '=' button")
def step_impl(context):
    context.page.click_normal_size()
@then ("It should be visible that the text from the page returns to its original state")
def step_impl(context):
    context.page.font_validation()
@when ("I click on the '-' button 8 times")
def step_impl(context):
    context.page.click_decrease()

@then ("It should be visible that the text in the page decreases its size")
def step_impl(context):
    context.page.font_decreases_validation()

@when ("I click on the 'Ridicat' button")
def step_impl(context):
    # raise NotImplementedError("STEP: When I click on the 'Ridicat' button")
    context.page.contrast_ridicat()

@then ("It should be visible that the contrast of the text on the page ensures easy and clear reading")
def step_impl(context):
    context.page.contrast_ridicat_validation()

@when ("I click on the 'Normal' button")
def step_impl(context):
    context.page.contrast_normal()

@then ("It should be visible that the text from the contrast page returns to its original state")
def step_impl(context):
    context.page.contrast_normal_validation()

@when ("I click on the 'Page Style' button")
def step_impl(context):
    context.page.page_style()

@when ("I click on the 'Black/White' button")
def step_impl(context):
    context.page.page_style_black_white()

@then ("It should be visible that the text on the page changes color in black and the background of the text in white")
def step_impl(context):
    context.page.page_style_black_white_validation()

@when ("I click on the 'White/Black' button")
def step_impl(context):
    context.page.page_style_white_black()

@then ("It should be visible that the text on the page changes color in white and the background of the text in black")
def step_impl(context):
    context.page.page_style_black_white_validation()

@when ("I click on the 'Yellow/Blue' button")
def step_impl(context):
    context.page.page_style_yellow_blue()

@then ("It should be visible that the text on the page changes color in yellow and the background of the text in blue")
def step_impl(context):
    context.page.page_style_yellow_blue_validation()

@when ("I click on the 'Standard' button")
def step_impl(context):
    context.page.page_style_standard()

@then ("It should be visible that the text from the page style returns to its original state")
def step_impl(context):
    context.page.page_style_standard_validation()