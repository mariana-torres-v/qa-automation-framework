Feature: Consulta de estado de cuenta

  Scenario: Consultar estado de cuenta del mes de Julio
    Given el usuario abre la aplicación
    When inicia sesion con una contraseña valida
    Then el sistema muestra el landing page

    When el usuario navega a "Estado de cuenta"
    And selecciona el año "2026"
    And selecciona el mes "Julio"
    And ingresa su contraseña
    And confirma la operación
    Then el sistema muestra el estado de cuenta solicitado
    And hay una opcion para descargarlo