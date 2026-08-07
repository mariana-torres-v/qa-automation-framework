from mobile.appium_driver import AppiumDriver

driver_manager = AppiumDriver()

driver = driver_manager.start()

print(driver.current_package)

driver_manager.stop()