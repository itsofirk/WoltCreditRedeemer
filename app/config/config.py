import os
from pathlib import Path

import yaml
from base64 import b64decode
from pydantic import BaseSettings, Field, validator


class AppConfig(BaseSettings):
    log_level = "INFO"
    app_name = __name__.split('.')[0]


class WoltWebsiteSettings(BaseSettings):
    class Config:
        env_prefix = "WOLT_"
    base_url = "https://wolt.com/en"
    redeem_path = "/me/redeem-code"

    show_login_form_button_text = "Log in"
    email_input_id = "method-select-email"
    send_email_button_text = "Next"
    promo_code_hint = "Enter promo code…"
    redeem_button_text = "Redeem"
    edge_user_data: str  # in windows, it's ...\AppData\Local\Microsoft\Edge\User Data


class GmailSettings(BaseSettings):
    class Config:
        env_prefix = "GMAIL_"

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings):
            return init_settings, env_settings, yaml_settings, file_secret_settings

    email: str = Field(...)
    app_password: str = Field(...)
    watch_folder: str = Field('Inbox')
    attachments_target: Path = Field(Path(os.getenv('APPDATA'), "WoltCreditRedeemer"))
    wolt_email = "info@wolt.com"
    subject = "הגיפט קארד של Wolt הגיע ומחכה לשליחה :)"
    pattern = r'CODE: (\w+)'
    group = 1

    @validator('app_password')
    def decode_password(cls, v):
        return b64decode(v)


def yaml_settings(settings: BaseSettings) -> dict[str, ...]:
    with open(os.getenv("CONFIG_FILE", 'app/config/config.yml')) as yml:
        data = yaml.safe_load(yml)
    return data[settings.__config__.env_prefix.lower().removesuffix('_')]
