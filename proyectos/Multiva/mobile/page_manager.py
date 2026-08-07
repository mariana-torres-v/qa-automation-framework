from proyectos.Multiva.mobile.pages.login_page import LoginPage
from proyectos.Multiva.mobile.pages.home_page import HomePage

from proyectos.Multiva.mobile.pages.administrar_destinatarios_page import (
    AdministrarDestinatariosPage
)

from proyectos.Multiva.mobile.pages.alta_destinatario_page import (
    AltaDestinatarioPage
)

from proyectos.Multiva.mobile.pages.confirmacion_page import (
    ConfirmacionPage
)

from proyectos.Multiva.mobile.pages.edit_destinatario_page import (
    EditDestinatarioPage
)

from proyectos.Multiva.mobile.pages.transferencias_page import (
    TransferenciasPage
)

from proyectos.Multiva.mobile.pages.movimientos_page import (
    MovimientosPage
)

from proyectos.Multiva.mobile.pages.estado_cuenta_page import (
    EstadoCuentaPage
)

class MobilePageManager:
    """
    Centraliza los Page Objects utilizados
    por la automatización mobile de Multiva.
    """

    def __init__(self, driver):

        self.login = LoginPage(driver)
        self.home = HomePage(driver)

        self.destinatarios = AdministrarDestinatariosPage(driver)
        self.alta_destinatario = AltaDestinatarioPage(driver)
        self.editar_destinatario = EditDestinatarioPage(driver)
        self.confirmacion = ConfirmacionPage(driver)

        self.transferencias = TransferenciasPage(driver)
        self.movimientos = MovimientosPage(driver)
        self.estado_cuenta = EstadoCuentaPage(driver)