from core.mobile.base_page import BasePageMobile
from proyectos.Multiva.mobile.locators.alta_destinatarios_locators import (
    AltaDestinatariosLocators as locators
)


class AltaDestinatarioPage(BasePageMobile):

    def click_new_recipient(self):
        self.click(
            locators.btn_new_recipient
        )

    def _input_product_number(self, product_number):
        self.write(
            locators.input_numero_producto,
            product_number
        )

        self.click(
            locators.btn_continue_product
        )

    def _input_name(self, name):
        self.write(
            locators.input_recipient,
            name
        )

    def _input_monthly_limit(self, monthly_limit):
        self.click(
            locators.input_mtu_container
        )

        self.write(
            locators.input_mtu,
            monthly_limit
        )

        self.hide_keyboard()

    def _input_alias(self, alias):
        self.write(
            locators.input_alias,
            alias
        )

    def _input_rfc(self, rfc):
        self.write(
            locators.input_rfc,
            rfc
        )

    def _input_email(self, email):
        self.write(
            locators.input_email,
            email
        )

        self.hide_keyboard()

    def fill_recipient(self, recipient):
        self._input_product_number(
            recipient["numero_producto"]
        )

        self._input_name(
            recipient["nombre"]
        )

        self._input_monthly_limit(
            recipient["monto_maximo"]
        )

        self._input_alias(
            recipient["alias"]
        )

        self._input_rfc(
            recipient["rfc"]
        )

        self._input_email(
            recipient["correo"]
        )

    def click_continue(self):
        self.click(
            locators.btn_continue_data
        )

    def click_confirm_operation(self):
        self.click(
            locators.btn_confirm_operation
        )