from playwright.sync_api import Page

class AlzaPage:
    def __init__(self, page: Page):
        self.page = page
        self.cookie_button = page.get_by_role("button", name="Rozumím")
        self.search_input = page.get_by_placeholder("Co hledáte?")
        self.search_button = page.get_by_test_id("button-search")
        self.buy_button = self.page.locator(".btnk1")
        self.continue_button = page.get_by_text("Pokračovat", exact=True)
        self.basket_icon = page.get_by_test_id("headerBasketIcon")

    def navigate(self):
        self.page.goto("https://www.alza.cz/", wait_until="domcontentloaded")

    def search_for(self, text: str):
        self.search_input.fill(text)
        self.search_button.click()

    def add_to_cart(self):
        self.buy_button.first.wait_for(state="visible", timeout=7000)
        self.buy_button.first.click() 