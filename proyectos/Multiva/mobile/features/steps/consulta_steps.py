from behave import when, then
from proyectos.Multiva.mobile import data


@when('selecciona una cuenta')
def step_seleccionar_cuenta(context):
    context.pages.home.go_to_account_details_page()


@when('selecciona el último movimiento "{tipo}"')
def step_seleccionar_ultimo_movimiento(context, tipo):

    if tipo == 'Terceros Multiva':
        amount = data.multiva_transfer_description

    elif tipo == 'SPEI':
        amount = data.spei_transfer_description

    elif tipo == 'Cuentas propias':
        amount = data.cuentas_propias_transfer_description

    else:
        raise ValueError(
            f"Tipo de destinatario no soportado: {tipo}"
        )

    context.pages.movements.click_on_last_movement(amount)


@then('el sistema muestra el comprobante del movimiento seleccionado')
def step_validar_comprobante_movimiento(context):
    context.pages.movements.is_comprobante_displayed()


@then('el usuario valida que el comprobante de la transferencia "{tipo}" es correcto')
def step_validar_el_comprobante_de_movimiento(context, tipo):

    if tipo == 'Terceros Multiva':
        description = data.multiva_transfer_description

    elif tipo == 'SPEI':
        description = data.spei_transfer_description

    elif tipo == 'Cuentas propias':
        description = data.cuentas_propias_transfer_description

    else:
        raise ValueError(
            f"Tipo de destinatario no soportado: {tipo}"
        )

    actual_description = context.pages.movements.get_transfer_description()
    assert description in actual_description, (
        f"El concepto de la transferencia es incorrecto. "
        f"Esperado que contenga: '{description}' | "
        f"Obtenido: '{actual_description}'"
    )