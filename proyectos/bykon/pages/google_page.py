from web.base_page import BasePage
from proyectos.bykon.locators.google_page_locators import GoogleLocators

class GooglePage(BasePage):

    def open_google(self):
        super().open()

    def search(self, text):
        self.fill(GoogleLocators.search_box, text)