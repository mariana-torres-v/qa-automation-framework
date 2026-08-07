Feature: Consulta de estado de cuenta

  Scenario: Consultar estado de cuenta del mes de Julio
    Given el usuario está en el landing page
    When selecciona una cuenta
    And navega a "Estados de cuenta"
    And selecciona el año "2026"
    And selecciona el mes "Julio"
    And ingresa su contraseña
    And confirma la operación
    Then el sistema muestra el estado de cuenta solicitado
    When solicita la descarga del estado de cuenta
    Then el estado de cuenta se descarga correctamente