from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators


class BasePage:

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_non_authorized_user(self):
        assert not self.is_element_present(*BasePageLocators.USER_AVATAR), "Пользователь авторизован в системе"
