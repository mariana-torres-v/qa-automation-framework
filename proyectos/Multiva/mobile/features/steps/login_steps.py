from behave import given, when, then
from proyectos.Multiva.mobile import data

from proyectos.Multiva.mobile.pages.login_page import LoginPage


from behave import when, then


@when('inicia sesión con una contraseña válida')
def step_login_password_valida(context):
    pass


@then('el usuario visualiza el landing page')
def step_visualiza_landing(context):
    pass


@then('el sistema muestra el saludo del usuario')
def step_validar_saludo(context):
    pass


#@given('el usuario abre la app')
#def step_impl(context):
#    context.login = LoginPage(context.driver)
#
#@when('el usuario da clic en "ingresar con contraseña"')
#def step_clic_ingresar(context):
#    context.login.click_login_with_password()
#
#@when('el usuario ingresa un "password" valido')
#def step_input_pass(context):
#    password = data.password
#    context.login.input_password(password)
#
#@when('el usuario hace clic en "Confirmar"')
#def step_clic_confirmar_login(context):
#    context.login.click_login()
#
#@then('el usuario visualiza la pantalla de inicio')
#def step_verify_home(context):
#    context.login.click_home()
#    assert context.home_is_displayed()