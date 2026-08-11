from behave import given, when, then

from proyectos.Multiva.mobile import data

# ============================================================
# COMMON STEPS
# ============================================================


@when('captura el "Número de producto" del destinatario "{tipo}"')
def step_capturar_producto(context, tipo):

    if tipo == "Multiva":
        product_number = data.multiva_product_number

    elif tipo == "SPEI":
        product_number = data.spei_product_number
    else:
        raise ValueError(
            f"Tipo de destinatario no soportado: {tipo}"
        )

    context.pages.destinatarios.write_product_number(
        product_number
    )
    context.pages.destinatarios.click_btn_next()


@when('captura los datos requeridos del destinatario "{tipo}"')
def step_capturar_datos_destinatario(context, tipo):

    if tipo == "Multiva":
        name = data.multiva_nombre
        mtu = data.mtu
        alias =data.multiva_alias

        context.pages.destinatarios.fill_recipient_multiva(
            name,
            mtu,
            alias
        )

    elif tipo == "SPEI":
        name = data.spei_nombre
        mtu = data.mtu
        alias = data.spei_alias
        rfc = data.rfc
        email = data.email

        context.pages.destinatarios.fill_recipient_spei(
            name,
            mtu,
            alias,
            rfc,
            email
        )

    else:
        raise ValueError(
            f"Tipo de destinatario no soportado: '{tipo}'"
        )

    context.recipient_name = name
    context.pages.destinatarios.scroll_and_click_btn_continue_button()


# ============================================================
# ALTA DESTINATARIOS
# ============================================================

@when('hace tap en "Agregar nuevo destinatario"')
def step_agregar_nuevo_destinatario(context):
    context.pages.destinatarios.click_btn_add_recipient()


@when('el usuario confirma el registro del destinatario')
def step_confirmar_registro_destinatario(context):
    context.pages.destinatarios.scroll_and_click_btn_confirm_operation()


@when('hace la validacion de identidad')
def step_ingresar_password(context):
    password = data.password
    context.pages.destinatarios.write_password(password)
    context.pages.destinatarios.click_btn_continue_auth()


@then('se muestra el modal "Por tu seguridad..."')
def step_validar_por_tu_seguridad_modal(context):
    assert context.pages.destinatarios.is_modal_30_min_displayed(), (
        f"No se muestra el modal 'Por tu seguridad...'"
    )


@then('finaliza la operación')
def step_finalizar_operacion_alta(context):

    context.pages.destinatarios.click_btn_finish()


@then('el destinatario "{tipo}" queda registrado')
def step_validar_destinatario_registrado(context, tipo):

    assert context.pages.confirmacion.is_recipient_name_displayed(
        context.recipient_name
    ), (
        f"No se encontró el destinatario '{tipo}' "
        f"con nombre '{context.recipient_name}'"
    )

# ============================================================
# EDICIÓN
# ============================================================

@when('el usuario selecciona un destinatario "{tipo}" para editar')
def step_seleccionar_destinatario(context, tipo):

    if tipo == "Multiva":
        alias = data.multiva_alias
    elif tipo == "SPEI":
        alias = data.spei_alias
    else:
        raise ValueError("Tipo de destinatario no soportado")

    context.pages.options.go_to_destinatarios_tab()
    context.pages.options.select_recipient(
        alias
    )

    context.pages.options.open_recipient_options()
    context.pages.options.click_opt_edit()


@when('el usuario modifica el MTU y Alias del destinatario "{tipo}"')
def step_modificar_datos_destinatario(context, tipo):

    mtu = data.mtu

    if tipo == 'Multiva':
        alias = data.multiva_modified_alias

    elif tipo == 'SPEI':
        alias = data.spei_modified_alias
    else:
        raise ValueError("Tipo de destinatario no soportado")

    context.pages.options.edit_mtu(mtu)
    context.pages.options.edit_alias(alias)

    context.pages.options.click_btn_confirm_edition()


@when('el usuario autoriza la operacion')
def step_autorizar_operacion(context):
    context.pages.destinatarios.write_password(data.password)
    context.pages.destinatarios.click_btn_continue_auth()


@then('el sistema manda un pop up de "operacion exitosa"')
def step_terminar_operacion(context):
    context.pages.options.click_accept_btn()


@then('el usuario regresa a la landing page')
def step_validar_destinatario_landing(context):
    context.pages.home.go_to_landing()


@when('finaliza la operación')
def step_finalizar_operacion_editar(context):
    context.pages.destinatarios.click_btn_finish()


@then('los datos del destinatario "{tipo}" se muestran actualizados')
def step_verificar_datos_destinatario_actualizados(context, tipo):

    if tipo == 'Multiva':
        new_alias = data.multiva_modified_alias

    elif tipo == 'SPEI':
        new_alias = data.spei_modified_alias
    else:
        raise ValueError("Tipo de destinatario no soportado")

    assert context.pages.options.is_updated_recipient_displayed(
        new_alias
    ), (
        f"No se encontró el destinatario con el nuevo nombre "
        f"'{new_alias}'"
    )


# ============================================================
# ELIMINACIÓN
# ============================================================

@when('el usuario selecciona un destinatario "{tipo}" para eliminar')
def step_seleccionar_destinatario_para_eliminar(context, tipo):

    if tipo == 'Multiva':
        alias = data.multiva_modified_alias

    elif tipo == 'SPEI':
        alias = data.spei_modified_alias

    else:
        raise ValueError(
            f"Tipo de destinatario no soportado: {tipo}"
        )

    context.pages.options.go_to_destinatarios_tab()
    context.pages.options.select_recipient(alias)
    context.pages.options.open_recipient_options()
    context.pages.options.click_opt_delete()


@when('el usuario confirma que desea eliminar al destinatario')
def step_confirmar_eliminar(context):
    context.pages.options.click_btn_confirm_delete()


@when('el usuario autoriza la eliminación')
def step_autorizar_eliminacion(context):
    context.pages.options.write_password_to_delete(
        data.password
    )
    context.pages.destinatarios.click_btn_continue_auth()


@then('el sistema manda un pop up de "eliminacion exitosa"')
def step_validar_eliminacion_exitosa(context):
    assert context.pages.options.is_delete_success_displayed(), (
        "No se mostró el mensaje de eliminación exitosa"
    )


@then('el destinatario "{tipo}" ya no se muestra en la lista de destinatarios')
def step_validar_destinatario_eliminado(context, tipo):

    if tipo == "Multiva":
        recipient_name = data.multiva_modified_alias

    elif tipo == "SPEI":
        recipient_name = data.spei_modified_alias

    else:
        raise ValueError(
            f"Tipo de destinatario no soportado: {tipo}"
        )

    assert not context.pages.options.is_recipient_displayed(
        recipient_name
    ), (
        f"El destinatario '{recipient_name}' "
        f"todavía aparece en la lista"
    )

