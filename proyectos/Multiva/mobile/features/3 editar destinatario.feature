Feature: Editar destinatario

@destinatarios @editar @spei @spei_e2e
Scenario: Modificar un destinatario SPEI

    Given el usuario abre la aplicación
    When inicia sesion con una contraseña valida
    Then el sistema muestra el landing page

    When el usuario navega a "Administrar destinatarios"
    And el usuario selecciona un destinatario "SPEI" para editar
    And el usuario modifica el MTU y Alias del destinatario "SPEI"

    Then el sistema manda un pop up de "operacion exitosa"
    And el usuario regresa a la landing page