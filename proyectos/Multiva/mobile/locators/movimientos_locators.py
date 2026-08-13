from appium.webdriver.common.appiumby import AppiumBy

class MovementsLocators:


    header_comprobante = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("VV00|contents1:S002-null-orgVoucher-flxHeaderSucess")'
    )

    @staticmethod
    def get_description_comprobante(text):
        return (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().textContains("{text}")'
    )
