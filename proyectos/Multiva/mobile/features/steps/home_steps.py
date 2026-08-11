from behave import then



@then('el sistema muestra el landing page')
def step_verify_home(context):
    assert context.pages.home.is_displayed()