import os
import pytest
from selene import browser
import dotenv


# @pytest.fixture(scope='function', autouse=True)
# def browser_settings():
#
#     browser.config.base_url = config.base_url
#     browser.config.driver_name = config.driver_name
#     browser.config.hold_driver_at_exit = config.hold_driver_at_exit
#     browser.config.window_width = config.window_width
#     browser.config.window_height = config.window_height
#     browser.config.timeout = config.timeout
#     yield
#     # browser.quit()


"""
Установка конфигураций используя pydantic
Инициализировали класс Config с установленными значениями конфигураций
В самой фикстуре вызываем класс Config и нужную опцию
"""


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    dotenv.load_dotenv()
    browser.config.driver_name = os.getenv('driver_name', 'chrome')
    browser.config.timeout = float(os.getenv('timeout', '4.0'))
    browser.config.base_url = os.getenv('base_url', 'https://demoqa.com/automation-practice-form')
    yield
    # browser.quit()


"""
Установка конфигураций используя библиотеку dotenv. Создаем файл .env, записываем туда значения конфигурация 
и потом вызываем значения в фикстуре через os.getenv, первое значение это название переменной в файле .env,
 второе значение по умолчанию 
"""