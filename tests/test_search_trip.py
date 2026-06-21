from playwright.sync_api import Page, expect
from pages.home_page import HomePage

def test_trip_search(page:Page):
    home = HomePage(page)
    home.open_url("https://www.bahn.de/")
    home.handle_cookie_banner()
    home.search_train("Berlin", "Hamburg")


