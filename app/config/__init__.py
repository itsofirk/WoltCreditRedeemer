from config import AppConfig, WoltWebsiteSettings
import logging

app_config = AppConfig()
logging.basicConfig(level=app_config.log_level)

wolt_settings = WoltWebsiteSettings()
