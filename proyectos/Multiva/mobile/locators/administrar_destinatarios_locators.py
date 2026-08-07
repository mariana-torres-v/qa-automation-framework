from appium.webdriver.common.appiumby import AppiumBy

class AdminDestinatariosLocators:

    @staticmethod
    def recipient_by_name(name):
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{name}")'
        )
    # locators.recipient_by_name("autodom5")
    # locators.recipient_by_name("autodom2")
    # locators.recipient_by_name("autodom1")

    @staticmethod
    def recipient_options(index):
        return (
            AppiumBy.ACCESSIBILITY_ID,
            f"VV01|contents1:S000-dtrAccountDestiny-{index}-icOptionMenu"
        )



    header_destinatarios = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01 | contents1:S000-null-frgHeader-txtTopBar'
    )

    btn_add_dest = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S000-btnNewOperation'
    )

    @staticmethod
    def recipient_options(index):
        return (
            AppiumBy.XPATH,
            f'//android.view.ViewGroup[@content-desc="VV01|contents1:S000-flcAccountDestiny{index}"]'
            '/android.view.View[@content-desc="VV01|contents1:S000-icOptionMenu"]'
        )
    # locators.recipient_options(0)


    btn_options = (
        AppiumBy.ACCESSIBILITY_ID,
        "VV01|contents1:S000-dtrAccountDestiny-0-icOptionMenu"
    )

    opt_edit_dest = (
        AppiumBy.ACCESSIBILITY_ID,
        "VV01|contents1:S000-flcEditar"
    )

    opt_delete_dest = (
        AppiumBy.ACCESSIBILITY_ID,
        "VV01|contents1:S000-txtEliminar"
    )

    btn_sure_to_delete = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S000-btnEliminar'
    )
"""Autorizar operacion"""
    input_password = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S002-null-frgInputPass-iptPassMdl'
    )
    btn_confirmar = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S002-btnEnable'
    )
