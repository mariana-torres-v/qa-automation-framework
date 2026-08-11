from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

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

    def is_element_displayed(self, locator, timeout=2):
        """Valida si el elemento es visible."""

        self.log.info(f"Validando si se muestra el elemento {locator}")

        try:
            element = WebDriverWait(
                self.driver,
                timeout
            ).until(
                EC.visibility_of_element_located(locator)
            )

            return element.is_displayed()

        except TimeoutException:
            self.log.info(f"Elemento no visible: {locator}")
            return False


    def scroll_into_view(self, locator):
        locator_type, locator_value = locator

        if locator_type == AppiumBy.ACCESSIBILITY_ID:
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                f'.scrollIntoView(new UiSelector().description("{locator_value}"))'
            )
            return

        raise ValueError(
            f"Tipo de locator no soportado para scroll: {locator_type}"
        )


    def scroll_and_click(self, locator):
        self.scroll_into_view(locator)
        self.click(locator)


    def scroll_into_view_by_text(self, text):
        # Busca un elemento por texto.
        # Si ya está visible, lo retorna directamente.
        # Si no está visible, intenta encontrarlo haciendo scroll.

        self.log.info(
            f"Buscando texto: '{text}'"
        )

        locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{text}")'
        )

        try:
            # Primero intenta encontrarlo sin hacer scroll
            element = self.driver.find_element(*locator)

            self.log.info(
                f"Texto encontrado sin scroll: '{text}'"
            )

            return element

        except NoSuchElementException:
            self.log.info(
                f"Texto no visible, buscando con scroll: '{text}'"
            )

            return self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true))'
                f'.scrollIntoView(new UiSelector().text("{text}"));'
            )


    def is_text_displayed_after_scroll(self, text):
        """Busca un texto haciendo scroll y devuelve si existe."""

        self.log.info(
            f"Buscando texto con scroll: '{text}'"
        )

        try:
            element = self.scroll_into_view_by_text(text)
            return element.is_displayed()

        except NoSuchElementException:
            self.log.info(
                f"No fue encontrado '{text}'"
            )
            return False


    def hide_keyboard(self):
        self.driver.execute_script('mobile:pressKey', {"keycode": 4})


    def get_text(self, locator):
        self.log.info(f"Tomando el texto del elemento '{locator}'")

        element = self.wait_for_element(locator)

        return element.text


    def element_contains_text(self, locator, expected_text):
        self.log.info(
            f"Validando que {locator} contenga '{expected_text}'"
        )

        actual_text = self.get_text(locator)

        self.log.info(
            f"Texto obtenido: '{actual_text}'"
        )

        return expected_text.lower() in actual_text.lower()

    def go_to_landing(self, max_attempts=5):
        """Regresa al landing page usando el botón Back."""

        if self.is_displayed():
            self.log.info("El usuario ya se encuentra en el landing page")
            return

        for attempt in range(1, max_attempts + 1):

            self.log.info(
                f"Intentando regresar al landing page "
                f"({attempt}/{max_attempts})"
            )

            self.driver.back()

            time.sleep(1)

            if self.is_displayed():
                self.log.info(
                    "El usuario regresó correctamente al landing page"
                )
                return

        raise AssertionError(
            f"No fue posible regresar al landing page "
            f"después de {max_attempts} intentos"
        )
