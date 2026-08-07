from core.browser import BrowserManager
from core.mobile.appium_driver import AppiumDriver

from proyectos.bykon.page_manager import PageManager
from proyectos.Multiva.mobile.page_manager import MobilePageManager


class EnvironmentManager:
    """
    Responsable de administrar el ciclo de vida
    de las ejecuciones web y mobile.
    """

    @staticmethod
    def before_all(context):

        platform = context.config.userdata.get("platform")

        if platform == "web":
            context.browser_manager = BrowserManager()
            context.page = context.browser_manager.start()
            context.pages = PageManager(context.page)

        elif platform == "mobile":
            context.appium_manager = AppiumDriver()
            context.driver = context.appium_manager.start()
            context.pages = MobilePageManager(context.driver)

        else:
            raise ValueError(
                "Debe indicarse platform=web o platform=mobile"
            )

    @staticmethod
    def after_all(context):

        if hasattr(context, "browser_manager"):
            context.browser_manager.stop()

        if hasattr(context, "appium_manager"):
            context.appium_manager.stop()