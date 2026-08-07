from core.config import Config
from core.waits import Waits

class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self, url: str = ""):
        """
        Abre la URL base o una ruta específica.
        """

        self.page.goto(f"{Config.BASE_URL}{url}")

    def get_title(self):
        """
        Devuelve el título de la página.
        """

        return self.page.title()

    def current_url(self):
        """
        Devuelve la url actual
        """

        return self.page.url

    def refresh(self):
        """
        Recarga la página.
        """

        self.page.reload()

    def wait(self, milliseconds=None):
        """
        Espera el timeout configurado.
        """

        self.page.wait_for_timeout(
            milliseconds or Config.TIMEOUT)

        # page.wait() #Espera lo que marca el TIMEOUT
        # page.wait(5000) #Espera lo que se desea

    def screenshot(self, path):
        """
        Guarda una captura.
        """

        return self.page.screenshot(path=path)


    """
    FUNCIONES DE INTERACCIÓN
    """

    def click(self, locator):
        """
        Hace click sobre un elemento
        """
        Waits.visible(self.page, locator)
        self.page.locator(locator).click()

    def fill(self, locator, text):
        """
        Escribe texto en un campo.
        """
        Waits.visible(self.page, locator)
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        """
        Devuelve el texto de un elemento.
        """
        Waits.visible(self.page, locator)
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator):
        """
        Indica si el elemento es visible.
        """
        return self.page.locator(locator).is_visible()

    def wait_for_element(self, locator):
        """
        Espera hasta que el elemento sea visible
        """
        self.page.locator(locator).wait_for(state="visible")

    def hover(self, locator):
        """
        Coloca el mouse
        """
        self.page.locator(locator).hover()

    def scroll_into_view(self, locator):
        """
        Hace scroll hasta el elemento.
        """
        self.page.locator(locator).scroll_into_view_if_needed()

    def get_attribute(self, locator, attribute):
        """
        Devuelve un atributo del elemento.
        """
        return self.page.locator(locator).get_attribute(attribute)

    def exists(self, locator):
        """
        Verifica si existe al menos un elemento que coincida con el locator.
        """
        return self.page.locator(locator).count() > 0

    