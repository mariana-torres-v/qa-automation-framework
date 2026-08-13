from proyectos.Multiva.mobile.pages.login_page import LoginPage
from proyectos.Multiva.mobile.pages.home_page import HomePage
from proyectos.Multiva.mobile.pages.admin_recipient_page import AdminDestinatariosPage
from proyectos.Multiva.mobile.pages.options_recipient_page import OptionsDestinatariosPage
from proyectos.Multiva.mobile.pages.movimientos_page import MovementsPage
from proyectos.Multiva.mobile.pages.transfer_page import TransferPage
from proyectos.Multiva.mobile.pages.account_statement_page import AccountStatementPage
from proyectos.Multiva.mobile.pages.popups_page import PopUpsPage
from proyectos.Multiva.mobile.pages.account_details_page import AccountDetailsPage


class MobilePageManager:

    def __init__(self, driver):
        self.login = LoginPage(driver)
        self.home = HomePage(driver)
        self.destinatarios = AdminDestinatariosPage(driver)
        self.options = OptionsDestinatariosPage(driver)
        self.movements = MovementsPage(driver)
        self.transfer = TransferPage(driver)
        self.account_statement = AccountStatementPage(driver)
        self.popups = PopUpsPage(driver)
        self.account_details = AccountDetailsPage(driver)
