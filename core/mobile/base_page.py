from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from core.logger.logging import FrameworkLogger

from appium.webdriver.common.appiumby import AppiumBy


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
            self.log.error(
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

    def scroll_into_view(self, locator):
        locator_type, locator_value = locator

        if locator_type == AppiumBy.ACCESSIBILITY_ID:
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true))'
                f'.scrollIntoView(new UiSelector().description("{locator_value}"));'
            )
        else:
            raise ValueError(
                f"Tipo de locator no soportado para scroll: {locator_type}"
            )

    def hide_keyboard(self):
        self.driver.execute_script('mobile:pressKey', {"keycode": 4})