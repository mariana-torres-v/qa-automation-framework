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
        options.app_package = Config.APP_PACKAGE
        options.app_activity = Config.APP_ACTIVITY

        options.no_reset = Config.NO_RESET
        options.force_app_launch = Config.FORCE_APP_LAUNCH

        self.logger.info("Iniciando sesión Appium")

        self.driver = webdriver.Remote(
            Config.APPIUM_SERVER,
            options=options
        )

        self.logger.info("Sesión Appium iniciada correctamente")

        self.driver.implicitly_wait(10)

        return self.driver

    def stop(self):

        if self.driver:
            self.logger.info("Cerrando sesión Appium")

            #if Config.CLOSE_APP_ON_EXIT:
             #   self.driver.terminate_app(Config.APP_PACKAGE)
            #self.logger.info("Se ha cerrado la app")

            self.driver.quit()