from proyectos.bykon.pages.google_page import GooglePage


class PageManager:

    def __init__(self, page):

        self.google = GooglePage(page)

    """
    from proyectos.bykon.pages.login_page import LoginPage
    from proyectos.bykon.pages.home_page import HomePage

    class PageManager:

        def __init__(self, page):
    
            self.login = LoginPage(page)

            self.home = HomePage(page)
        """