from behave import given, when, then

@given('el usuario abre la aplicación')
def step_abrir_aplicacion(context):
    pass


@given('el usuario se encuentra en el landing page')
def step_usuario_en_landing(context):
    assert context.pages.home.is_displayed()


@then('el sistema muestra la pantalla "{pantalla}"')
def step_validar_pantalla(context, pantalla):

    if pantalla == "Confirmación de la operación":
        assert context.pages.destinatarios.is_confirmation_visible(), (
            "No se mostró la pantalla de confirmación"
        )

        recipient_name = (
            context.pages.destinatarios.get_recipient_name()
        )

        assert recipient_name == context.recipient_name, (
            f"Nombre incorrecto. "
            f"Esperado: '{context.recipient_name}', "
            f"Obtenido: '{recipient_name}'"
        )

    elif pantalla == "Operación exitosa":
        success_message = "Operación exitosa"

        gotten_message = (
            context.pages.destinatarios.get_success_message()
        )

        assert success_message == gotten_message, (
            f"No se realizó la operación correctamente. "
            f"Mensaje esperado: '{success_message}', "
            f"Mensaje obtenido: '{gotten_message}'"
        )

    else:
        raise ValueError(
            f"Pantalla no soportada: '{pantalla}'"
        )


@when('el usuario navega a "{option}"')
def step_navegar_a(context, option):

    if option == "Administrar destinatarios":
        context.pages.home.click_btn_transferir()
        context.pages.home.go_to_administrar_destinatarios()

    elif option == "Transferir terceros":
        context.pages.home.click_btn_transferir()
        context.pages.home.click_transferir_terceros()

    elif option == "Transferir cuentas propias":
        context.pages.home.click_btn_transferir()
        context.pages.home.click_transferir_cuentas_propias()

    elif option == "Movimientos":
        context.pages.home.go_to_account_details_page()

    elif option == "Estado de cuenta":
        context.pages.home.go_to_account_details_page()
        context.pages.account_details.open_account_statements_page()




@when('selecciona la opción "{opcion}"')
def step_seleccionar_opcion(context, opcion):
    pass


@when('el sistema muestra la pantalla "{screen}"')
def step_ingresar_password(context, screen):

    if screen == "Operacion exitosa":
        return context.pages.options.is_header_operacion_exitosa_displayed()

    elif screen == "Autorizar operacion":
        return context.pages.destinatarios.is_header_autorizar_operacion_displayed()


@then('el usuario cierra el pop up "{tipo}"')
def step_cerrar_popup(context, tipo):
    if tipo == "Rate your experience":
        context.pages.popups.close_rate_experience_if_displayed()

    else:
        pass


@when('confirma la operación')
def step_confirmar_operacion(context):
    pass


@then('el sistema regresa al landing page')
def step_validar_regreso_landing(context):
    pass


@then('el sistema muestra el resultado de la operación')
def step_validar_resultado_operacion(context):
    pass