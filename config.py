import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    base_url: str = 'https://demoqa.com/automation-practice-form'
    driver_name: str = 'chrome'
    hold_driver_at_exit: bool = False
    window_width: int = 1920
    window_height: int = 1080
    timeout: float = 3.0


config = Config()

