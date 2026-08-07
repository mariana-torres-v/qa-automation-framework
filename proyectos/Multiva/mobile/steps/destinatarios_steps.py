from behave import when, then


@when('captura los datos requeridos del destinatario "{tipo}"')
def step_capturar_datos_destinatario(context, tipo):
    pass


@when('selecciona un destinatario "{tipo}"')
def step_seleccionar_destinatario(context, tipo):
    pass


@when('modifica los datos permitidos del destinatario')
def step_modificar_datos_destinatario(context):
    pass


@when('continúa con el registro')
def step_continuar_registro(context):
    pass


@when('continúa con la modificación')
def step_continuar_modificacion(context):
    pass


@when('confirma el registro del destinatario')
def step_confirmar_registro_destinatario(context):
    pass


@when('confirma la eliminación')
def step_confirmar_eliminacion(context):
    pass


@when('acepta el resultado de la operación')
def step_aceptar_resultado(context):
    pass


@then('el destinatario "{tipo}" queda registrado')
def step_validar_destinatario_registrado(context, tipo):
    pass


@then('los datos del destinatario se muestran actualizados')
def step_validar_destinatario_actualizado(context):
    pass


@then('el destinatario "{tipo}" ya no se muestra en la lista')
def step_validar_destinatario_eliminado(context, tipo):
    pass