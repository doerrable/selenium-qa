import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    opts = Options()
    # Headless in CI or when HEADLESS=1
    if os.getenv("HEADLESS", "").strip() == "1":
        opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--start-maximized")
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    drv.implicitly_wait(0)
    yield drv
    drv.quit()
