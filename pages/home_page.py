from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from datetime import datetime, timedelta

class HomePage(BasePage):

    def __init__(self, page:Page):
        super().__init__(page)

        self.from_input = page.get_by_label("Start")
        self.to_input = page.get_by_label("Ziel")
        self.search_button = page.get_by_role("button", name="Suchen")

    def search_train(self, origin: str,
                     destination: str,
                     first_class:bool = False,
                     today:bool = True,
                     one_way:bool = True):

        self.from_input.click()
        self.from_input.fill(origin)
        self.page.get_by_text(origin, exact=False).first.click()

        self.to_input.click()
        self.to_input.fill(destination)
        self.page.get_by_text(destination, exact=False).first.click()

        if first_class:
            self.page.get_by_role("option", name="1. Klasse").click()


        if not today:
            tomorrow_date = datetime.now() + timedelta(days=1)
            tomorrow = str(tomorrow_date.day)

            self.page.get_by_text("Heute, ab").click()
            active_month = self.page.locator(".db-web-date-picker-calendar .swiper-slide-active")
            active_month.get_by_text(tomorrow, exact=True).click()
            self.page.locator("[data-test-id=\"undefined-save-button\"]").click()

            expect(self.page.locator(".quick-finder-options__hinfahrt .quick-finder-option-area__heading")).to_contain_text("Morgen")


        if not one_way:
            tomorrow_date = datetime.now() + timedelta(days=1)
            tomorrow = str(tomorrow_date.day)

            self.page.get_by_text("Heute, ab").click()
            self.page.locator(".quick-finder-zeitauswahl-content__time-picker-bar").get_by_role("button", name="jetzt").click()

            self.page.get_by_text("Rückfahrt").click()
            active_month = self.page.locator(".db-web-date-picker-calendar .swiper-slide-active")
            active_month.get_by_text(tomorrow, exact=True).click()
            self.page.locator("[data-test-id=\"undefined-save-button\"]").click()

        self.page.get_by_role("button", name="Suchen").click()

