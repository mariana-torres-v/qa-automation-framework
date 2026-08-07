from behave import when, then


@when('selecciona una cuenta')
def step_seleccionar_cuenta(context):
    pass


@when('consulta los movimientos de la cuenta')
def step_consultar_movimientos(context):
    pass


@when('selecciona el último movimiento')
def step_seleccionar_ultimo_movimiento(context):
    pass


@then('el sistema muestra el comprobante del movimiento seleccionado')
def step_validar_comprobante_movimiento(context):
    pass