from core.mobile.base_page import BasePageMobile
from proyectos.Multiva.mobile.locators.home_locators import HomeLocators as locators


class HomePage(BasePageMobile):

    def is_displayed(self):
        return self.is_element_displayed(
            locators.title_home
        )

    # ===========================
    # Cuentas
    # ===========================

    def go_to_account_details_page(self):
        self.click(
            locators.cuenta_basica_gf
        )

    # ===========================
    # SNACK BAR -- $ TRANSFERIR $
    # ===========================

    def click_btn_transferir(self):
        self.click(
            locators.btn_transferir
        )

    def go_to_administrar_destinatarios(self):
        self.click(
            locators.btn_admin_destinatarios
        )

    def click_transferir_cuentas_propias(self):
        self.click(
            locators.btn_cuentas_propias
        )

    def click_transferir_terceros(self):
        self.click(
            locators.btn_terceros
        )

    # ===========================
    # Logout
    # ===========================

    def click_btn_hamburguesa(self):
        self.click(
            locators.menu_hamburguesa
        )

    def click_opt_logout(self):
        self.click(
            locators.opt_logout
        )

    def click_btn_logout(self):
        self.click(
            locators.btn_logout
        )

    def logout(self):
        self.click_btn_hamburguesa()
        self.click_opt_logout()
        self.click_btn_logout()

