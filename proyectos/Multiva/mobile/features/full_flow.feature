Feature: Recorrido E2E de operación bancaria

  @e2e
  Scenario: Completar el recorrido de operación bancaria
    Given el usuario inicia sesión correctamente

    When da de alta un destinatario Multiva
    Then el destinatario queda registrado correctamente

    When modifica el destinatario Multiva
    Then los datos del destinatario se actualizan correctamente

    When realiza una transferencia al destinatario
    Then la transferencia se realiza correctamente

    When consulta el último movimiento de la cuenta
    Then el sistema muestra el comprobante del movimiento seleccionado

    When consulta el estado de cuenta del periodo seleccionado
    Then el sistema muestra el estado de cuenta solicitado

    When elimina el destinatario Multiva
    Then el destinatario deja de mostrarse en la lista


