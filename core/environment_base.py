from core.browser import BrowserManager
from proyectos.bykon.page_manager import PageManager

class EnvironmentManager:
    """
    Responsabale de administrar el ciclo de vida del navegador.
    """

    @staticmethod
    def before_all(context):

        context.browser_manager = BrowserManager()
        context.page = context.browser_manager.start()
        context.pages = PageManager(context.page)

        """
        Behave tiene tres objetos disponibles 
        context.browser_manager
        context.page
        context.pages
        """

    @staticmethod
    def after_all(context):

        if hasattr(context, "browser_manager"):
            context.browser_manager.stop()


