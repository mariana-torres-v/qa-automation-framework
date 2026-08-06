from core.config import Config

print(Config.BASE_URL)
print(Config.BROWSER)
print(Config.HEADLESS)
print(Config.TIMEOUT)

from core.browser import BrowserManager

browser = BrowserManager()

page = browser.start()

page.goto("https://playwright.dev")

print(page.title())

browser.stop()

