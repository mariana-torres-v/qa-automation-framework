from behave import when, then
from proyectos.Multiva.mobile import data


@when('el usuario navega a transferir a terceros')
def step_usuario_navega_transferir(context):
    context.pages.home.click_btn_transferir()
    context.pages.home.click_transferir_terceros()


@when('el usuario captura los datos requeridos de la transferencia "{tipo}"')
def step_capturar_datos_transferencia(context, tipo):

    if tipo == 'Terceros Multiva':
        amount = data.multiva_transfer_amount
        description = data.multiva_transfer_description
        alias = data.forever_multiva_alias

        context.pages.transfer.open_selector_cuenta_origen()
        context.pages.transfer.select_cuenta_origen()
        context.pages.transfer.open_selector_cuenta_destino()
        context.pages.transfer.select_cuenta_destino(alias)
        context.pages.transfer.tap_importe()
        context.pages.transfer.write_importe(amount)
        context.pages.transfer.write_description(description)

    elif tipo == 'SPEI':
        amount = data.multiva_transfer_amount
        description = data.multiva_transfer_description
        alias = data.forever_multiva_alias

        context.pages.transfer.open_selector_cuenta_origen()
        context.pages.transfer.select_cuenta_origen()
        context.pages.transfer.open_selector_cuenta_destino()
        context.pages.transfer.select_cuenta_destino(alias)
        context.pages.transfer.tap_importe()
        context.pages.transfer.write_importe(amount)
        context.pages.transfer.write_description(description)

    elif tipo == 'Cuentas propias':
        amount = data.cuentas_propias_amount
        description = data.cuentas_propias_transfer_description
        alias = data.propia_alias

        context.pages.transfer.select_cuenta_propia_origen()
        context.pages.transfer.open_selector_cuenta_propia_destino()
        context.pages.transfer.select_cuenta_destino(alias)
        context.pages.transfer.input_importe_to_cuenta_propia(amount)
        context.pages.transfer.input_concepto_propia(description)

    else:
        raise ValueError(f"Tipo de destinatario no soportado: {tipo}")


@when('el usuario continúa con la transferencia "{tipo}"')
def step_continuar_transferencia(context, tipo):

    if tipo in ("Terceros Multiva", "SPEI"):
        context.pages.transfer.click_btn_continuar()
    elif tipo == "Cuentas propias":
        context.pages.transfer.click_continue_to_confirmation()

    else:
        raise ValueError(
            f"Tipo de destinatario no soportado: {tipo}"
        )


@when('el usuario confirma la transferencia "{tipo}"')
def step_confirmar_transferencia(context, tipo):

    if tipo in ("Terceros Multiva", "SPEI"):
        assert context.pages.transfer.confirmation_header_is_displayed(), (
            "No se muestra la pantalla de confirmación de la transferencia"
        )
        context.pages.transfer.click_btn_confirmar()

    elif tipo == "Cuentas propias":
        assert context.pages.transfer.confirmation_header_is_displayed_propias(), (
            "No se muestra la pantalla de confirmación de la transferencia a cuentas propias"
        )
        context.pages.transfer.click_btn_confirmar_propias()

    else:
        raise ValueError(
            f"Tipo de destinatario no soportado: {tipo}"
        )


@when('el usuario autoriza la transferencia')
def step_autorizar_transferencia(context):
    context.pages.transfer.write_password(data.password)
    context.pages.transfer.click_btn_autorizar()


@then('el usuario ve el comprobante de la transferencia')
def step_ver_comprobante_transferencia(context):
    assert context.pages.transfer.header_success_is_displayed()


@then('el usuario finaliza la transferencia')
def step_finalizar_transferencia(context):
    context.pages.transfer.click_btn_finish()


@then('el usuario ve el comprobante de la transferencia "Cuentas propias"')
def step_comprobante_transferencia_cuentas_propias(context):
    assert context.pages.transfer.is_comprobante_displayed()

@then('el usuario finaliza la transferencia "Cuentas propias"')
def step_finalizar_transferencia_cuentas_propias(context):
    context.pages.transfer.click_btn_finalizar_propias()