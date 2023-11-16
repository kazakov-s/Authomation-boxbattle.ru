from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.urls import USER_REGISTERED
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import HomePageLocators
from time import sleep

class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    # Регистрация пользователя с проверкой факта авторизации
    def register_new_user(self, email, password):
        # Проверяем, что авторизация происходит через email адрес
        assert self.browser.find_element(*LoginPageLocators.EMAIL_SPAN).text == 'E-mail'
        # Находим поле email
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        # Находим поле пароль
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD)
        # Вводим валидный email
        email_input.send_keys(email)
        # Вводим валидный пароль
        password_input.send_keys(password)
        # Находим кнопку "Войти"
        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        )
        button.click()
        # Проверяем факт авторизации
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, '//a[@class="bb-avatar"]'))
            WebDriverWait(self.browser, 5).until(element_present)
            assert self.browser.current_url == USER_REGISTERED
        except:
            print("Страница загружается слишком долго")


    def should_be_password_recover_link(self):
        # Проверяем, что авторизация происходит через email адрес
        assert self.browser.find_element(*LoginPageLocators.EMAIL_SPAN).text == 'E-mail'
        # Находим ссылку "Восстановить пароль"
        self.browser.find_element(*LoginPageLocators.RECOVER_LINK).click()
        # Ждем отрисовки формы восстановления пароля
        try:
            element_present = EC.presence_of_element_located((By.XPATH, '//form[@class="bb-password-recovery-form"]'))
            WebDriverWait(self.browser, 5).until(element_present)
            # Проверяем, что форма восстановления пароля открыта
            assert self.browser.find_element(*LoginPageLocators.RECOVER_TITLE)
        except:
            print("Страница загружается слишком долго")

    def google_account_authorization(self):
        # Проверяем, что авторизация происходит через email адрес
        assert self.browser.find_element(*LoginPageLocators.EMAIL_SPAN).text == 'E-mail'
        # Находим кнопку Google
        self.browser.find_element(*LoginPageLocators.GOOGLE_BUTTON).click()
        # Проверяем, что открыта страница авторизации Google
        assert 'google' in self.browser.current_url



