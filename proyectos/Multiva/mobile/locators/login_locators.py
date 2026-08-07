from appium.webdriver.common.appiumby import AppiumBy

class LoginLocators:

    btn_login_w_pass = (
        AppiumBy.ACCESSIBILITY_ID,
        "VV16|contents1:S000-flcLoginWithPass"
    )

    text_password = (
        AppiumBy.ACCESSIBILITY_ID,
        "VV16|contents1:S000-orgInputPass-iptPassMdl"
    )

    btn_login = (
        AppiumBy.ACCESSIBILITY_ID,
        "VV16|contents1:S000-btnLogin"
    )
