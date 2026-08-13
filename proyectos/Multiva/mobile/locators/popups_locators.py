from appium.webdriver.common.appiumby import AppiumBy

class PopUpsLocators:

    header_rate_experience = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Califica tu experiencia con nuestra aplicación")'
    )

    btn_en_otro_momento = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("VV01|contents1:S007-btnSecundary")'
    )