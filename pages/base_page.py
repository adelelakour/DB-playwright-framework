class BasePage:
    def __init__(self, page):
        self.page = page
        self.cookie_accept_btn = page.get_by_role("button", name="Allow all cookies")

    def open_url(self, url: str):
        self.page.goto(url)

    def handle_cookie_banner(self):
        try:
            self.cookie_accept_btn.wait_for(state="visible", timeout=5000)
            self.cookie_accept_btn.click()
            print("✅ Cookie banner accepted successfully.")
        except Exception:
            print("⚠️ Cookie banner did not appear or was already accepted. Proceeding...")



