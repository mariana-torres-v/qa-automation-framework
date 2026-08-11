from behave import when, then
from proyectos.Multiva.mobile import data


@when('el usuario navega a transferir a terceros')
def step_usuario_navega_transferir(context):
    context.pages.home.click_btn_transferir()
    context.pages.home.click_transferir_terceros()

@when('el usuario navega a transferir a cuentas propias')


@when('el usuario captura los datos requeridos de la transferencia "{tipo}"')
def step_capturar_datos_transferencia(context, tipo):


    context.pages.transfer.open_selector_cuenta_origen()
    context.pages.transfer.select_cuenta_origen()

    if tipo == 'Terceros Multiva':
        amount = data.multiva_transfer_amount
        description = data.multiva_transfer_description
        context.pages.transfer.open_selector_cuenta_destino()
        context.pages.transfer.select_cuenta_destino_multiva()

    elif tipo == 'SPEI':
        amount = data.spei_transfer_amount
        description = data.spei_transfer_description
        alias = data.forever_spei_alias
        context.pages.transfer.open_selector_cuenta_destino()
        context.pages.transfer.select_cuenta_destino_spei(alias)

    elif tipo == 'Cuentas propias':
        amount = data.cuentas_propias_amount
        description = data.cuentas_propias_transfer_description
        context.pages.transfer.open_selector_cuenta_destino()
        context.pages.transfer.select_cuenta_propia()

    else:
        raise ValueError(
            f"Tipo de destinatario no soportado: {tipo}"
        )

    context.pages.transfer.tap_importe()
    context.pages.transfer.write_importe(amount)
    context.pages.transfer.write_description(description)


@when('el usuario continúa con la transferencia')
def step_continuar_transferencia(context):
    context.pages.transfer.click_btn_continuar()


@when('el usuario confirma la transferencia')
def step_confirmar_transferencia(context):
    context.pages.transfer.confirmation_header_is_displayed()
    context.pages.transfer.click_btn_confirmar()


@when('el usuario autoriza la transferencia')
def step_autorizar_transferencia(context):
    context.pages.transfer.write_password(data.password)
    context.pages.transfer.click_btn_autorizar()


@then('el usuario ve el comprobante de la transferencia')
def step_ver_comprobante_transferencia(context):
    context.pages.transfer.header_success_is_displayed()


@when('finaliza la transferencia')
def step_finalizar_transferencia(context):
    context.pages.transfer.click_btn_finish()