from behave import when, then


@when('selecciona el año "{anio}"')
def step_seleccionar_anio(context, anio):
    pass


@when('selecciona el mes "{mes}"')
def step_seleccionar_mes(context, mes):
    pass


@when('solicita la descarga del estado de cuenta')
def step_descargar_estado_cuenta(context):
    pass


@then('el sistema muestra el estado de cuenta solicitado')
def step_validar_estado_cuenta(context):
    pass


@then('el estado de cuenta se descarga correctamente')
def step_validar_descarga_estado_cuenta(context):
    pass