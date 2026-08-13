Feature: Consulta de movimientos

  @consulta @movimientos @cuentas_propias
  Scenario: Consultar el último movimiento de una cuenta - Cuentas propias

    Given el usuario abre la aplicación
    When inicia sesion con una contraseña valida
    Then el sistema muestra el landing page

    When selecciona una cuenta
    And selecciona el último movimiento "Cuentas propias"
    Then el sistema muestra el comprobante del movimiento seleccionado
    And el usuario valida que el comprobante de la transferencia "Cuentas propias" es correcto


  @consulta @movimientos @terceros_multiva
  Scenario: Consultar el último movimiento de una cuenta - Terceros Multiva

    Given el usuario abre la aplicación
    When inicia sesion con una contraseña valida
    Then el sistema muestra el landing page

    When selecciona una cuenta
    And selecciona el último movimiento "Terceros Multiva"
    Then el sistema muestra el comprobante del movimiento seleccionado
    And el usuario valida que el comprobante de la transferencia "Terceros Multiva" es correcto

  @consulta @movimientos @spei
  Scenario: Consultar el último movimiento de una cuenta - SPEI

    Given el usuario abre la aplicación
    When inicia sesion con una contraseña valida
    Then el sistema muestra el landing page

    When selecciona una cuenta
    And selecciona el último movimiento "SPEI"
    Then el sistema muestra el comprobante del movimiento seleccionado
    And el usuario valida que el comprobante de la transferencia "SPEI" es correcto