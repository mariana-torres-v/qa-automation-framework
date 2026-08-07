Feature: Login

    @login @smoke
    Scenario: Iniciar sesión correctamente
        Given el usuario abre la aplicación
        When inicia sesión con una contraseña válida
        Then el usuario visualiza el landing page


