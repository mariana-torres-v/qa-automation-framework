from behave import then

from proyectos.Multiva.mobile.pages.home_page import HomePage


@then('el usuario visualiza el landing page')
def step_verify_home(context):
    assert context.pages.home.is_displayed()