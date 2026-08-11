from appium.webdriver.common.appiumby import AppiumBy

class AdminDestinatariosLocators:

    header_recipients = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S000-null-frgHeader-txtTopBar'
    )


    header_recipients = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S000-null-frgHeader-txtTopBar'
    )

    tab_destinatarios = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S000-flcRecipientsDis'
    )

    tab_favoritos = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S000-flcFavoritesDis'
    )

    btn_add_recipient = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S000-btnNewOperation'
    )

    # OPCIONES

    @staticmethod
    def recipient_by_name(name):
        # encuentra un destinatario por nombre
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{name}")'
        )

    @staticmethod
    def btn_recipient_options(index):
        return (
            AppiumBy.XPATH,
            f'//android.view.ViewGroup'
            f'[@content-desc="VV01|contents1:S000-flcAccountDestiny{index}"]'
            f'/android.view.View'
            f'[@content-desc="VV01|contents1:S000-icOptionMenu"]'
        )


    opt_edit = (
        AppiumBy.ACCESSIBILITY_ID,
        "VV01|contents1:S000-flcEditar"
    )


    # -------------------------------------------------------------------
    # ALTA
    # -------------------------------------------------------------------

    # # INGRESAR PRODUCTO
    input_product_number = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S001-null-frgInputAccount-iptValue'
    )

    btn_next  = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S001-btnContinue'
    )


    # # # FORMULARIO AÑADIR DESTINATARIO
    input_name = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S010-null-frgInputNameDestiny-iptValue'
    )

    tap_mtu = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S010-null-iptAmountMax-flcInput'
    )

    input_mtu = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S010-null-iptAmountMax-iptValue'
    )

    input_alias = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S010-null-frgInputNameAlias-iptValue'
    )

    input_rfc = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S010-null-frgInputRFC-iptValue'
    )

    input_email =(
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S010-null-frgInputEmail-iptValue'
    )

    switch_add_favorite = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S010-null-iptSwitchFavorite-flcContainerSwitchOFF'
    )

    btn_continue = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S010-btnContinue'
    )

    #------------------------------------------------------------------
    # CONFIRMA LA OPERACIÓN
    # ------------------------------------------------------------------
    header_confirm_operation = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S004-null-orgVoucher-txtHeaderInfo'
    )

    @staticmethod
    def recipient_name(name):
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{name}")'
        )

    btn_confirm_operation = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S004-null-orgBtnPrimary-btnPrimary'
    )

    # ------------------------------------------------------------------
    # AUTORIZACION
    # ------------------------------------------------------------------

    input_password = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S002-null-frgInputPass-iptPassMdl'
    )


    btn_continue_auth = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S002-btnEnable'
    )

    # ------------------------------------------------------------------
    # OPERACIÓN EXITOSA
    # ------------------------------------------------------------------

    header_success_operation = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Comprobante de operación")'
    )

    btn_finish = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S006-btnFinish'
    )

    btn_add_other_account = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S006-btnNext'
    )

    # -------------------------------------------------------------------
    # EDITAR
    # -------------------------------------------------------------------

    input_edit_mtu = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S007-null-iptAmountMax-iptValue'
    )

# TODO REVISAR APPIUM INSPECTO PARA SABER CUÁL ES EL LOCATOR CORRECTO DE...
    input_edit_alias = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S007-null-frgInputNameAlias-iptValue'
    )

    btn_confirm_edition = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S007-btnContinue'
    )

    btn_accept = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S007-null-orgPopup-btnActionPopup'
    )

    # -------------------------------------------------------------------
    # ELIMINAR
    # -------------------------------------------------------------------

    opt_delete = (
        AppiumBy.ACCESSIBILITY_ID,
        "VV01|contents1:S000-txtEliminar"
    )

    btn_si_eliminar = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S000-btnEliminar'
    )


    btn_sure_to_delete = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S000-btnEliminar'
    )

    input_pass_to_delete = (
        AppiumBy.ACCESSIBILITY_ID,
        'VV01|contents1:S002-null-frgInputPass-iptPassMdl'
    )
