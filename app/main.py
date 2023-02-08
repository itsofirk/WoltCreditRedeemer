import os
from time import sleep

from config import gmail_settings as g
from wolt_crawler import perform_login, redeem_code
from email_listener import EmailListener
from email_helper import filter_messages, extract_code


def process_messages(messages):
    for message in messages:
        code = extract_code(message, g.pattern, g.group)
        # TODO: finish following function
        # redeem_code(code)
        # for now, prints codes to console
        print(code)


def main():
    print("Process PID: " + str(os.getpid()))
    g.attachments_target.mkdir(parents=True, exist_ok=True)
    email = EmailListener(g.email, g.app_password, g.watch_folder, g.attachments_target)
    email.login()
    scraped_messages = email.scrape(unread=True)
    filter_generator = filter_messages(scraped_messages, g.wolt_email, g.subject)
    process_messages(filter_generator)
    email.listen(60, process_messages, unread=True)


if __name__ == '__main__':
    main()
