from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class HomePage(BasePage):

    def __init__(self, page:Page):
        super().__init__(page)

        self.from_input = page.get_by_label("Start")
        self.to_input = page.get_by_label("Ziel")
        self.search_button = page.get_by_role("button", name="Suchen")

    def search_train(self, origin: str, destination: str):
        self.from_input.click()
        self.from_input.fill(origin)
        self.page.get_by_text(origin, exact=False).first.click()

        self.to_input.click()
        self.to_input.fill(destination)
        self.page.get_by_text(destination, exact=False).first.click()

        self.page.get_by_role("button", name="Suchen").click()
