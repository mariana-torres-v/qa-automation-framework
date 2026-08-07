from core.browser import BrowserManager
from web.base_page import BasePage

browser = BrowserManager()

page = browser.start()

base_page = BasePage(page)

base_page.open()

print(base_page.get_title())

print(base_page.current_url())

browser.stop()