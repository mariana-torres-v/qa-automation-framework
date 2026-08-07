Feature: Consulta de movimientos

  @consulta @movimientos
  Scenario: Consultar el último movimiento de una cuenta
    Given el usuario se encuentra en el landing page
    When selecciona una cuenta
    And consulta los movimientos de la cuenta
    And selecciona el último movimiento
    Then el sistema muestra el comprobante del movimiento seleccionado