from .base_page import BasePage

class InventoryPage(BasePage):
    def on_page(self) -> bool:
        return self.url_contains("/inventory.html")
