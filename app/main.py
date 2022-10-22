from config import gmail_settings as g
from wolt_crawler import perform_login
from email_listener import EmailListener


def main():
    email = EmailListener(g.email, g.app_password, g.watch_folder, g.attachments_target)
    # 1. auth wolt
    perform_login(g.email)
    # 2. get login link from email
    # 3. open redeem page
    # 4. redeem promo
    ...


if __name__ == '__main__':
    main()
