from proyectos.Multiva.mobile.pages.login_page import LoginPage
from proyectos.Multiva.mobile.pages.home_page import HomePage
from proyectos.Multiva.mobile.pages.administrar_destinatarios_page import AdministrarDestinatariosPage
from proyectos.Multiva.mobile.pages.transferencias_page import TransferenciasPage
from proyectos.Multiva.mobile.pages.movimientos_page import MovimientosPage
from proyectos.Multiva.mobile.pages.estado_cuenta_page import EstadoCuentaPage


class MobilePageManager:
    """
    Centraliza la creación de los Page Objects móviles.
    Cada página comparte la misma instancia del driver.
    """

    def __init__(self, driver):

        self.login = LoginPage(driver)

        self.home = HomePage(driver)

        self.destinatarios = AdministrarDestinatariosPage(driver)

        self.transferencias = TransferenciasPage(driver)

        self.movimientos = MovimientosPage(driver)

        self.estado_cuenta = EstadoCuentaPage(driver)