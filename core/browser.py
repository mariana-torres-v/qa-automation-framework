from playwright.sync_api import sync_playwright
from core.config import Config
from core.logging.logger import FrameworkLogger


class BrowserManager:
    """
    Responsable de iniciar y cerrar playwright
    """

    def __init__(self):

        self.playwright = None
        self.browser = None
        self.contexto = None
        self.page = None

        self.logger = FrameworkLogger.get_logger()

    def start(self):
        """Inicia Playwright y abre el navegador."""
        self.playwright = sync_playwright().start()

        if Config.EXECUTION_ENV == "local":
            return self._start_local()

        elif Config.EXECUTION_ENV == "browserstack":
            return self._start_browserstack()

        else:
            raise ValueError(
                f"Entorno '{Config.EXECUTION_ENV}' no soportado."
            )

    def _start_local(self):

        if Config.BROWSER == "chromium":
            self.browser = self.playwright.chromium.launch(
                headless = Config.HEADLESS
            )

        elif Config.BROWSER == "firefox":
            self.browser = self.playwright.firefox.launch(
                headless = Config.HEADLESS
            )

        elif Config.BROWSER == "webkit":
            self.browser = self.playwright.webkit.launch(
                headless = Config.HEADLESS
            )

        else:
            raise ValueError(
                f"Navegador '{Config.BROWSER}' no soportado."
            )

        self.page = self.browser.new_page()

        self.page.set_default_timeout(Config.TIMEOUT)

        return self.page


    def _start_browserstack(self):

        raise NotImplementedError(
            "La integración con BrowserStack se implementará más adelante.")

        #ws_endpoint = ...
        #
        #self.browser = self.playwright.chromium.connect(
        #    ws_endpoint=ws_endpoint
        #)
        #
        #self.page = self.browser.new_page()
        #
        #return self.page


    def stop(self):
        """Cierra el navegador y Playwright."""

        if self.page:
            self.page.close()

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()

