from behave import then

from proyectos.Multiva.mobile.pages.home_page import HomePage


@then('el usuario visualiza la pantalla principal')
def step_verify_home(context):
    context.home = HomePage(context.driver)

    assert context.home.is_displayed()