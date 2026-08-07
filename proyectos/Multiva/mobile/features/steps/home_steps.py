from behave import then

from proyectos.Multiva.mobile.pages.home_page import HomePage


@given('el usuario se encuentra en el landing page')
def step_usuario_en_landing(context):
    assert context.pages.home.is_displayed()

@then('el usuario visualiza el landing page')
def step_verify_home(context):
    assert context.pages.home.is_displayed()