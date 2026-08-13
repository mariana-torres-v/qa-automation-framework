Feature: Login

    @login
    Scenario: Iniciar sesión correctamente

        Given el usuario abre la aplicación
        When inicia sesion con una contraseña valida
        Then el sistema muestra el landing page

