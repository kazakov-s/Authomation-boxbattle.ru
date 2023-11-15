from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.urls import USER_REGISTERED
from .base_page import BasePage
from .locators import LoginPageLocators
from time import sleep


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD)
        email_input.send_keys(email)
        password_input.send_keys(password)
        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        )
        button.click()
        sleep(3)
        assert self.browser.current_url == USER_REGISTERED
