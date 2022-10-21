from pydantic import BaseSettings, Field


class AppConfig(BaseSettings):
    log_level = "INFO"
    app_name = __name__.split('.')[0]


class WoltWebsiteSettings(BaseSettings):
    class Config:
        env_prefix = "WOLT_"
    base_url = "https://wolt.com/en"
    redeem_path = "/me/redeem-code"

    login_button_text = "Log in"
    promo_code_hint = "enter promo code..."
    redeem_button_text = "redeem"


