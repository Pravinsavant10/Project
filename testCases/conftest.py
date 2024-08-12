import pytest as pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://bankapp.credence.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver
