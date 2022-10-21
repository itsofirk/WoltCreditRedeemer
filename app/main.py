from config import credentials
from wolt_crawler import perform_login


def main():
    # 1. auth wolt
    perform_login(credentials.email)
    # 2. get login link from email
    # 3. open redeem page
    # 4. redeem promo
    ...


if __name__ == '__main__':
    main()
