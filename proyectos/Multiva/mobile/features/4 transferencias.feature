Feature: Transferencias

  # ============================================================
  # CUENTAS PROPIAS
  # ============================================================

  @transferencias @cuentas_propias
  Scenario: Realizar una transferencia entre "Cuentas propias"

    Given el usuario abre la aplicación
    When inicia sesion con una contraseña valida
    Then el sistema muestra el landing page

    When el usuario navega a transferir a cuentas propias
    And el usuario captura los datos requeridos de la transferencia "Cuentas propias"
    And el usuario continúa con la transferencia
    And el usuario confirma la transferencia
    And el usuario autoriza la transferencia
    And confirma la operación

    Then el usuario ve el comprobante de la transferencia
    And finaliza la transferencia

  # ============================================================
  # TERCEROS MULTIVA
  # ============================================================

  @transferencias @terceros_multiva
  Scenario: Realizar una transferencia a un tercero Multiva

    Given el usuario abre la aplicación
    When inicia sesion con una contraseña valida
    Then el sistema muestra el landing page

    When el usuario navega a transferir a terceros
    And el usuario captura los datos requeridos de la transferencia "Terceros Multiva"
    And el usuario continúa con la transferencia
    And el usuario confirma la transferencia
    And el usuario autoriza la transferencia
    And confirma la operación

    Then el usuario ve el comprobante de la transferencia
    And finaliza la transferencia



  # ============================================================
  # SPEI
  # ============================================================

  @transferencias @spei
  Scenario: Realizar una transferencia SPEI

    Given el usuario abre la aplicación
    When inicia sesion con una contraseña valida
    Then el sistema muestra el landing page

    When el usuario navega a transferir a terceros
    And el usuario captura los datos requeridos de la transferencia "SPEI"
    And el usuario continúa con la transferencia
    And el usuario confirma la transferencia
    And el usuario autoriza la transferencia
    And confirma la operación

    Then el usuario ve el comprobante de la transferencia
    And finaliza la transferencia

