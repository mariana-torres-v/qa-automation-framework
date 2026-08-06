Feature: Validar arquitectura del framework

  Scenario: Abrir Google

    Given que abro Google
    When busco "Playwright"
    Then la página contiene "Playwright"