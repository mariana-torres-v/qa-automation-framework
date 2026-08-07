from appium.webdriver.common.appiumby import AppiumBy

class HomeLocators:

    title_home = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Hola, Nombre!")'
    )


    cuenta_basica_gf = (
        AppiumBy.ACCESSIBILITY_ID,
        "VV00|contents1:S002-dtgRowProd0-0-flcCardProduct0"
    )

    cuenta_multiva = (
        AppiumBy.ACCESSIBILITY_ID,
        ''
    )

    cuenta_integra = (
        AppiumBy.ACCESSIBILITY_ID,
        ''
    )

    btn_transferir = (
        AppiumBy.ACCESSIBILITY_ID,
        "VV00|contents1:S002-flcFooterMenuTransf"
    )

    btn_cuentas_propias = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description('
        '"VV00|contents1:S002-idrMenuTrransfer-rptItem"'
        ').instance(0)'
    )

    btn_terceros = (
        AppiumBy.ACCESSIBILITY_ID,
        'new UiSelector().description('
        '"VV00|contents1:S002-idrMenuTrransfer-rptItem"'
        ').instance(1)'
    )

    btn_admin_destinatarios = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description('
        '"VV00|contents1:S002-idrMenuTrransfer-rptItem"'
        ').instance(2)'
    )

    menu_hamburguesa = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        ''
    )

    opt_logout = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        ''
    )

    btn_logout = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        ''
    )