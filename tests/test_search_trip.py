from playwright.sync_api import Page, expect
from pages.home_page import HomePage


class TestSeachHappyPath:

    def test_basic_trip_search(self, page):
        home = HomePage(page)
        home.open_url("https://www.bahn.de/")
        home.handle_cookie_banner()
        home.search_train("Berlin", "Hamburg")

    def test_first_class_trip_search(self, page):
        home = HomePage(page)
        home.open_url("https://www.bahn.de/")
        home.handle_cookie_banner()
        home.search_train("Berlin", "Hamburg", True)

    def test_tomorrow_trip_search(self, page):
        home = HomePage(page)
        home.open_url("https://www.bahn.de/")
        home.handle_cookie_banner()
        home.search_train("Berlin", "Hamburg", today=False)
