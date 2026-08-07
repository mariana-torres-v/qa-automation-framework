from core.mobile.base_page import BasePageMobile
from proyectos.Multiva.mobile.locators.home_locators import HomeLocators as locators


class HomePage(BasePageMobile):

    def is_displayed(self):
        return self.is_element_displayed(locators.title_home)
