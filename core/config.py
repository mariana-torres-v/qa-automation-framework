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

    # ===== Appium =====

    APPIUM_SERVER = os.getenv(
        "APPIUM_SERVER",
        "http://127.0.0.1:4723"
    )

    PLATFORM_NAME = os.getenv(
        "PLATFORM_NAME",
        "Android"
    )

    AUTOMATION_NAME = os.getenv(
        "AUTOMATION_NAME",
        "UiAutomator2"
    )

    DEVICE_NAME = os.getenv(
        "DEVICE_NAME",
        "Android"
    )

    APP_PACKAGE = os.getenv(
        "APP_PACKAGE",
        "net.veritran.mvmx.p3.qa"
    )

    APP_ACTIVITY = os.getenv(
        "APP_ACTIVITY",
        "net.veritran.mvmx.p3.qa.VTCommonActivity"
    )

    NO_RESET = os.getenv(
        "NO_RESET",
        "True"
    ).lower() == "true"

    FORCE_APP_LAUNCH = os.getenv(
        "FORCE_APP_LAUNCH",
        "True"
    ).lower() == "true"

    #CLOSE_APP_ON_EXIT = True


    # ===== BrowserStack =====
    BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME", "")
    BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY", "")
    BROWSERSTACK_PROJECT = os.getenv("BROWSERSTACK_PROJECT", "QA Framework")
    BROWSERSTACK_BUILD = os.getenv("BROWSERSTACK_BUILD", "Build Local")
    BROWSERSTACK_SESSION_NAME = os.getenv(
        "BROWSERSTACK_SESSION_NAME",
        "Playwright Test"
    )