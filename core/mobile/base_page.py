from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from core.logger.logging import FrameworkLogger


class BasePageMobile:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = FrameworkLogger.get_logger()

    def wait_for_element(self, locator) -> WebElement:
        """Espera hasta que el elemento sea visible."""
        self.log.info(f"Esperando elemento {locator}")

        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            )

        except TimeoutException:
            self.log.error(
                f"Timeout esperando elemento visible | "
                f"Locator: {locator} | "
                f"Timeout: 10 segundos"
            )
            raise

    def wait_for_clickable(self, locator) -> WebElement:
        """Espera hasta que el elemento pueda recibir un clic."""
        self.log.info(f"Esperando elemento {locator} para hacer clic")

        try:
            return self.wait.until(
                EC.element_to_be_clickable(locator)
            )

        except TimeoutException:
            logger.error(
                f"Timeout esperando elemento clickeable | "
                f"Locator: {locator} | "
                f"Timeout: 10 segundos"
            )
            raise

    def click(self, locator):
        """Espera el elemento y hace clic."""
        self.log.info(f"Clic en {locator}")

        element = self.wait_for_clickable(locator)
        element.click()

    def write(self, locator, text):
        """Espera el elemento y escribe texto."""
        self.log.info(f"Se escribe dentro de {locator}")

        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def is_element_displayed(self, locator):
        """Valida que el elemento sea visible."""
        self.log.info(f"Esperando que se muestre el elemento {locator}")

        return self.wait_for_element(locator).is_displayed()