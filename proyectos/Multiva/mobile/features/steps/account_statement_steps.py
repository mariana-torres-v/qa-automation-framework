from behave import when, then

from proyectos.Multiva.mobile import data


@when('selecciona el año "{anio}"')
def step_seleccionar_anio(context, anio):
    context.pages.account_statement.select_year(anio)


@when('selecciona el mes "{mes}"')
def step_seleccionar_mes(context, mes):
    context.pages.account_statement.select_month(mes)


@when('ingresa su contraseña')
def step_ingresar_password_estado_cuenta(context):
    context.pages.account_statement.input_password(data.password)
    context.pages.account_statement.click_confirmar()


@when('solicita la descarga del estado de cuenta')
def step_descargar_estado_cuenta(context):
    context.pages.account_statement.click_descargar()


@then('el sistema muestra el estado de cuenta solicitado')
def step_validar_estado_cuenta(context):
    assert context.pages.account_statement.is_displayed(), (
        "No se muestra el estado de cuenta solicitado"
    )


@then('hay una opcion para descargarlo')
def step_validar_opcion_descarga(context):
    assert context.pages.account_statement.is_download_option_displayed(), (
        "No se muestra la opción para descargar el estado de cuenta"
    )


@then('el estado de cuenta se descarga correctamente')
def step_validar_descarga_estado_cuenta(context):
    assert context.pages.account_statement.is_download_option_displayed(), (
        "No se muestra la opción para descargar el estado de cuenta"
    )