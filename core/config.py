import os


class Config:
    """Configuración general del framework."""

    # Tipo de ejecución
    EXECUTION_ENV = os.getenv("EXECUTION_ENV", "local").lower()

    # Plataforma de automatización
    PLATFORM = os.getenv("PLATFORM", "web").lower()

    # URL base del proyecto
    BASE_URL = os.getenv("BASE_URL", "https://www.google.com")

    # Navegador
    BROWSER = os.getenv("BROWSER", "chromium").lower()

    # Headless
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"

    # Timeout general (milisegundos)
    TIMEOUT = int(os.getenv("TIMEOUT", "30000"))

    # Screenshots
    SCREENSHOT_ON_FAILURE = True

    # ===== BrowserStack =====
    BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME", "")
    BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY", "")
    BROWSERSTACK_PROJECT = os.getenv("BROWSERSTACK_PROJECT", "QA Framework")
    BROWSERSTACK_BUILD = os.getenv("BROWSERSTACK_BUILD", "Build Local")
    BROWSERSTACK_SESSION_NAME = os.getenv(
        "BROWSERSTACK_SESSION_NAME",
        "Playwright Test"
    )