from appium import webdriver
from appium.options.android import UiAutomator2Options

from core.config import Config
from core.logger.logging import FrameworkLogger


class AppiumDriver:

    def __init__(self):
        self.driver = None
        self.logger = FrameworkLogger.get_logger()

    def start(self):
        options = UiAutomator2Options()

        options.platform_name = Config.PLATFORM_NAME
        options.automation_name = Config.AUTOMATION_NAME
        options.device_name = Config.DEVICE_NAME

        options.set_capability(
            "appium:appPackage",
            Config.APP_PACKAGE
        )

        options.set_capability(
            "appium:appActivity",
            Config.APP_ACTIVITY
        )

        options.set_capability(
            "appium:noReset",
            True
        )

        options.set_capability(
            "appium:forceAppLaunch",
            True
        )

        options.set_capability(
            "appium:autoLaunch",
            True
        )

        self.logger.info("Iniciando sesión Appium")

        self.driver = webdriver.Remote(
            Config.APPIUM_SERVER,
            options=options
        )

        self.logger.info("Sesión Appium iniciada correctamente")
        self.logger.info(
            f"App activa: {self.driver.current_package}"
        )

        self.driver.implicitly_wait(10)

        return self.driver

    def stop(self):

        if self.driver:
            self.logger.info("Cerrando sesión Appium")
            self.driver.quit()