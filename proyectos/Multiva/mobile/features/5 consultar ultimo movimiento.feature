Feature: Consulta de movimientos

  @consulta @movimientos @spei
  Scenario: Consultar el último movimiento de una cuenta

    Given el usuario abre la aplicación
    When inicia sesion con una contraseña valida
    Then el sistema muestra el landing page

    When selecciona una cuenta
    And selecciona el último movimiento "SPEI"
    Then el sistema muestra el comprobante del movimiento seleccionado
    And el usuario valida que el comprobante de la transferencia "{tipo}" es correcto