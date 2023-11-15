from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_AVATAR = (By.PARTIAL_LINK_TEXT, 'avatar')


class LoginPageLocators:
    EMAIL = (By.XPATH, '//input[@type="text"]')
    PASSWORD = (By.XPATH, '//input[@type="password"]')
    BUTTON_SUBMIT = (By.XPATH, '//button[@type="submit"]')
