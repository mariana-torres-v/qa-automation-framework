from behave import when, then

from proyectos.Multiva.mobile import data


@when('inicia sesión con una contraseña válida')
def step_login_password_valida(context):
    password = data.password

    context.pages.login.click_login_with_password()
    context.pages.login.input_password(password)
    context.pages.login.click_login()



