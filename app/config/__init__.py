from .config import AppConfig, WoltWebsiteSettings, GmailSettings
import logging

app_config = AppConfig()
wolt_settings = WoltWebsiteSettings()
gmail_settings = GmailSettings()


logging.basicConfig(level=app_config.log_level)
