from behave import when

from proyectos.Multiva.mobile import data


@when('inicia sesion con una contraseña valida')
def step_login_password_valida(context):
    password = data.password

    context.pages.login.click_login_with_password()
    context.pages.login.input_password(password)
    context.pages.login.click_login()



