from behave import given, when, then

@given('el usuario abre la aplicación')
def step_abrir_aplicacion(context):
    pass


@given('el usuario se encuentra en el landing page')
def step_usuario_en_landing(context):
    pass


@given('el usuario se encuentra en "{pantalla}"')
def step_usuario_en_en_pantalla(context, pantalla):
    pass


@when('navega a "{opcion}"')
def step_navegar_a(context, opcion):
    pass


@when('selecciona la opción "{opcion}"')
def step_seleccionar_opcion(context, opcion):
    pass


@when('ingresa su contraseña')
def step_ingresar_password(context):
    pass


@when('confirma la operación')
def step_confirmar_operacion(context):
    pass


@then('el sistema muestra la pantalla "{pantalla}"')
def step_validar_pantalla(context, pantalla):
    pass


@then('el sistema regresa al landing page')
def step_validar_regreso_landing(context):
    pass

@then('el sistema muestra el resultado de la operación')
def step_validar_resultado_operacion(context):
    pass