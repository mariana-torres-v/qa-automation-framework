
from core.mobile.base_page import BasePageMobile
from proyectos.Multiva.mobile.locators.movimientos_locators import MovementsLocators as locators

class MovementsPage(BasePageMobile):


    def click_on_last_movement(self, amount):
        element = self.scroll_into_view_by_text(amount)
        element.click()


    def is_comprobante_displayed(self):
        self.is_element_displayed(locators.header_comprobante)


    def get_transfer_description(self):
        locator = locators.description
        actual_description = self.get_text(locator)
        return actual_description


    def back_to_home_page_from_movement_description(self):
        self.hide_keyboard()
        self.hide_keyboard()
