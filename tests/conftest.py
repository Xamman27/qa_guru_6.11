import pytest
from selene import browser
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    base_url: str = 'https://demoqa.com/automation-practice-form'
    driver_name: str = 'chrome'
    hold_driver_at_exit: bool = False
    window_width: int = 1920
    window_height: int = 1080
    timeout: float = 3.0





@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    config = Config()
    browser.config.base_url = config.base_url
    browser.config.driver_name = config.driver_name
    browser.config.hold_driver_at_exit = config.hold_driver_at_exit
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.timeout = config.timeout
    yield
    # browser.quit()

