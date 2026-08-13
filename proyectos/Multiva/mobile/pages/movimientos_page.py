from core.mobile.base_page import BasePageMobile
from proyectos.Multiva.mobile.locators.movimientos_locators import MovementsLocators as locators

class MovementsPage(BasePageMobile):

    def is_comprobante_displayed(self):
        return self.is_element_displayed(locators.header_comprobante)


    def is_description_displayed(self, description):
        locator = locators.get_description_comprobante(description)
        return self.is_element_displayed(locator)


    def back_to_home_page_from_movement_description(self):
        self.hide_keyboard()
        self.hide_keyboard()