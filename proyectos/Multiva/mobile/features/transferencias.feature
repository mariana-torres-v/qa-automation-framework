Feature: Transferencias

  # ============================================================
  # CUENTAS PROPIAS
  # ============================================================

  @transferencias @cuentas_propias
  Scenario: Realizar una transferencia entre cuentas propias
    Given el usuario se encuentra en el landing page
    When navega a "Transferir"
    And selecciona la opción "Cuentas propias"
    And captura los datos requeridos de la transferencia
    And continúa con la transferencia
    Then el sistema muestra la pantalla "Confirmación de la operación"
    When confirma la transferencia
    And ingresa su contraseña
    And confirma la operación
    Then el sistema muestra la pantalla "Operación exitosa"
    When finaliza la transferencia
    Then el sistema regresa al landing page


  # ============================================================
  # TERCEROS MULTIVA
  # ============================================================

  @transferencias @terceros_multiva
  Scenario: Realizar una transferencia a un tercero Multiva
    Given el usuario se encuentra en el landing page
    When navega a "Transferir"
    And selecciona la opción "Terceros"
    And captura los datos requeridos de la transferencia
    And continúa con la transferencia
    Then el sistema muestra la pantalla "Confirmación de la operación"
    When confirma la transferencia
    And ingresa su contraseña
    And confirma la operación
    Then el sistema muestra la pantalla "Operación exitosa"
    When finaliza la transferencia
    Then el sistema regresa al landing page


  # ============================================================
  # SPEI
  # ============================================================

  @transferencias @spei
  Scenario: Realizar una transferencia SPEI
    Given el usuario se encuentra en el landing page
    When navega a "Transferir"
    And selecciona la opción "SPEI"
    And captura los datos requeridos de la transferencia
    And continúa con la transferencia
    Then el sistema muestra la pantalla "Confirmación de la operación"
    When confirma la transferencia
    And ingresa su contraseña
    And confirma la operación
    Then el sistema muestra la pantalla "Operación exitosa"
    When finaliza la transferencia
    Then el sistema regresa al landing page

