from behave import given, when, then

from proyectos.Multiva.mobile import data


# ============================================================
# NAVEGACIÓN / ADMINISTRACIÓN
# ============================================================

@given('el usuario se encuentra en "Administrar destinatarios"')
def step_usuario_en_administrar_destinatarios(context):
    assert context.pages.destinatarios.is_displayed()


@when('navega a "Administrar destinatarios"')
def step_navegar_administrar_destinatarios(context):
    context.pages.home.go_to_administrar_destinatarios()


# ============================================================
# ALTA
# ============================================================

@when('selecciona la opción "Agregar nuevo destinatario"')
def step_agregar_nuevo_destinatario(context):
    context.pages.destinatarios.click_add_new_recipient()


@when('captura los datos requeridos del destinatario "{tipo}"')
def step_capturar_datos_destinatario(context, tipo):

    recipient = data.destinatarios[tipo]

    context.pages.alta_destinatario.fill_recipient(
        recipient
    )

@when('continúa con el registro')
def step_continuar_registro(context):
    context.pages.alta_destinatario.click_continue()


@then('el sistema muestra la pantalla "Confirmación de la operación"')
def step_validar_confirmacion_operacion(context):
    assert context.pages.confirmacion.is_displayed()


@when('confirma el registro del destinatario')
def step_confirmar_registro_destinatario(context):
    context.pages.alta_destinatario.click_confirm_operation()


@when('ingresa su contraseña')
def step_ingresar_password(context):

    context.pages.confirmacion.input_password(
        password
    )


@when('confirma la operación')
def step_confirmar_operacion(context):
    context.pages.confirmacion.click_confirm_operation()


@then('el sistema muestra la pantalla "Operación exitosa"')
def step_validar_operacion_exitosa(context):
    assert context.pages.confirmacion.is_success_displayed()


@when('finaliza la operación')
def step_finalizar_operacion(context):
    context.pages.confirmacion.click_finish()


@then('el destinatario "{tipo}" queda registrado')
def step_validar_destinatario_registrado(context, tipo):

    destinatario = data.destinatarios[tipo]

    assert context.pages.destinatarios.recipient_is_displayed(
        destinatario
    )


# ============================================================
# EDICIÓN
# ============================================================

@when('selecciona un destinatario "{tipo}"')
def step_seleccionar_destinatario(context, tipo):
    destinatario = data.destinatarios[tipo]

    context.pages.destinatarios.select_recipient(
        destinatario
    )

    context.pages.destinatarios.open_recipient_options()


@when('selecciona la opción "Editar"')
def step_seleccionar_editar(context):
    context.pages.destinatarios.click_edit()


@when('modifica los datos permitidos del destinatario')
def step_modificar_datos_destinatario(context):

    datos_modificados = data.destinatario_modificado

    context.pages.editar_destinatario.edit_allowed_data(
        datos_modificados
    )


@when('continúa con la modificación')
def step_continuar_modificacion(context):
    context.pages.editar_destinatario.click_continue()


@then('los datos del destinatario se muestran actualizados')
def step_validar_datos_actualizados(context):

    datos_modificados = data.destinatario_modificado

    assert context.pages.destinatarios.updated_data_is_displayed(
        datos_modificados
    )


# ============================================================
# ELIMINACIÓN
# ============================================================

@when('selecciona la opción "Eliminar"')
def step_seleccionar_eliminar(context):
    context.pages.destinatarios.click_delete()


@when('confirma la eliminación')
def step_confirmar_eliminacion(context):
    context.pages.destinatarios.confirm_delete()


@when('acepta el resultado de la operación')
def step_aceptar_resultado(context):
    context.pages.confirmacion.click_finish()


@then('el destinatario "{tipo}" ya no se muestra en la lista')
def step_validar_destinatario_eliminado(context, tipo):

    destinatario = data.destinatarios[tipo]

    assert not context.pages.destinatarios.recipient_is_displayed(
        destinatario
    )