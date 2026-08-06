from core.config import Config

class Waits:

    @staticmethod
    def visible(page, locator):
        """
        Espera hasta que el elemento sea visible.
        """
        page.locator(locator).wait_for(
            state="visible",
            timeout=Config.TIMEOUT
        )

        @staticmethod
        def hidden(page, locator):
            """
            Espera hasta que elemento desaparezca.
            """
            page.locator(locator).wait_for(
                state="hidden",
                timeout=Config.TIMEOUT
            )

        @staticmethod
        def attached(page, locator):
            """
            Espera a que el elemento exista en el DOM.
            """
            page.locator(locator).wait_for(
                state="attached",
                timeout=Config.TIMEOUT
            )

        @staticmethod
        def detached(page, locator):
            """
            Espera a que el elemento sea eliminado del DOM.
            """
            page.locator(locator).wait_for(
                state="detached",
                timeout=Config.TIMEOUT
            )

