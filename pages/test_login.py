from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

USER = "standard_user"
PASS = "secret_sauce"

def test_login_success(driver):
    login = LoginPage(driver).open()
    login.login(USER, PASS)
    inv = InventoryPage(driver)
    assert inv.on_page(), "Expected to land on inventory page after login"

def test_login_failure_shows_error(driver):
    login = LoginPage(driver).open()
    login.login("bad_user", "bad_pass")
    msg = login.error_text().lower()
    assert "username and password do not match" in msg or "epic sadface" in msg
