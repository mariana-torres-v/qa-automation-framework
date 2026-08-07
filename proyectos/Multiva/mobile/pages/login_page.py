
from core.mobile.base_page import BasePageMobile
from proyectos.Multiva.mobile.locators.login_locators import LoginLocators as locators


class LoginPage(BasePageMobile):

    def click_login_with_password(self):
        self.click(locators.btn_login_w_pass)


    def input_password(self, password):
        self.write(locators.text_password, password)


    def click_login(self):
        self.click(locators.btn_confirmar)



