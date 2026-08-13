from behave import when, then
from proyectos.Multiva.mobile import data


@when('selecciona una cuenta')
def step_seleccionar_cuenta(context):
    context.pages.home.go_to_account_details_page()


@when('selecciona el último movimiento "{tipo}"')
def step_seleccionar_ultimo_movimiento(context, tipo):

    if tipo == 'Terceros Multiva':
        amount = data.multiva_transfer_amount

    elif tipo == 'SPEI':
        amount = data.spei_transfer_amount

    elif tipo == 'Cuentas propias':
        amount = data.cuentas_propias_amount

    else:
        raise ValueError(
            f"Tipo de destinatario no soportado: {tipo}"
        )

    context.pages.account_details.click_on_last_movement_by_type(amount)


@then('el sistema muestra el comprobante del movimiento seleccionado')
def step_validar_comprobante_movimiento(context):
    assert context.pages.movements.is_comprobante_displayed(), (
        "No se muestra el comprobante del movimiento seleccionado"
    )


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

    assert context.pages.movements.is_description_displayed(description), (
        f"No se muestra el comprobante con la descripción esperada: '{description}'"
    )