Feature: Administración de destinatarios

  # ============================================================
  # ALTA
  # ============================================================

  @destinatarios @alta @multiva
  Scenario: Dar de alta un destinatario Multiva
    Given el usuario se encuentra en el landing page
    When navega a "Administrar destinatarios"
    And selecciona la opción "Agregar nuevo destinatario"
    And captura los datos requeridos del destinatario "Multiva"
    And continúa con el registro
    Then el sistema muestra la pantalla "Confirmación de la operación"
    When confirma el registro del destinatario
    And ingresa su contraseña
    And confirma la operación
    Then el sistema muestra la pantalla "Operación exitosa"
    And el destinatario "Multiva" queda registrado


  @destinatarios @alta @otro_banco
  Scenario: Dar de alta un destinatario de otro banco
    Given el usuario se encuentra en el landing page
    When navega a "Administrar destinatarios"
    And selecciona la opción "Agregar nuevo destinatario"
    And captura los datos requeridos del destinatario "Otro banco"
    And continúa con el registro
    Then el sistema muestra la pantalla "Confirmación de la operación"
    When confirma el registro del destinatario
    And ingresa su contraseña
    And confirma la operación
    Then el sistema muestra la pantalla "Operación exitosa"
    And el destinatario "Otro banco" queda registrado


  # ============================================================
  # MODIFICACIÓN
  # ============================================================

  @destinatarios @editar @multiva
  Scenario: Modificar un destinatario Multiva
    Given el usuario se encuentra en "Administrar destinatarios"
    When selecciona un destinatario "Multiva editar"
    And selecciona la opción "Editar"
    And modifica los datos permitidos del destinatario
    And continúa con la modificación
    Then el sistema muestra la pantalla "Operación exitosa"
    And los datos del destinatario se muestran actualizados


  @destinatarios @editar @otro_banco
  Scenario: Modificar un destinatario de otro banco
    Given el usuario se encuentra en "Administrar destinatarios"
    When selecciona un destinatario "Otro banco editar"
    And selecciona la opción "Editar"
    And modifica los datos permitidos del destinatario
    And continúa con la modificación
    Then el sistema muestra la pantalla "Operación exitosa"
    And los datos del destinatario se muestran actualizados


  # ============================================================
  # ELIMINACIÓN
  # ============================================================

  @destinatarios @eliminar @multiva
  Scenario: Eliminar un destinatario Multiva
    Given el usuario se encuentra en "Administrar destinatarios"
    When selecciona un destinatario "Multiva eliminar"
    And selecciona la opción "Eliminar"
    And confirma la eliminación
    And ingresa su contraseña
    And confirma la operación
    Then el sistema muestra la pantalla "Operación exitosa"
    When acepta el resultado de la operación
    Then el destinatario "Multiva" ya no se muestra en la lista


  @destinatarios @eliminar @otro_banco
  Scenario: Eliminar un destinatario de otro banco
    Given el usuario se encuentra en "Administrar destinatarios"
    When selecciona un destinatario "Otro banco eliminar"
    And selecciona la opción "Eliminar"
    And confirma la eliminación
    And ingresa su contraseña
    And confirma la operación
    Then el sistema muestra la pantalla "Operación exitosa"
    When acepta el resultado de la operación
    Then el destinatario "Otro banco" ya no se muestra en la lista

