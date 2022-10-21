from .config import AppConfig, WoltWebsiteSettings, Credentials
import logging

app_config = AppConfig()
wolt_settings = WoltWebsiteSettings()
credentials = Credentials()


logging.basicConfig(level=app_config.log_level)
