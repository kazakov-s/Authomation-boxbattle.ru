from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_AVATAR = (By.PARTIAL_LINK_TEXT, 'avatar')

class LoginPageLocators:
    EMAIL_SPAN = (By.CLASS_NAME, 'bb-text.e-placeholder.text-body-16-22.color-on-surface-70')
    EMAIL = (By.XPATH, '//input[@type="text"]')
    PASSWORD = (By.XPATH, '//input[@type="password"]')
    BUTTON_SUBMIT = (By.XPATH, '//button[@type="submit"]')
    RECOVER_LINK = (By.XPATH, '//button[@class="e-recovery-button"]')
    RECOVER_TITLE = (By.XPATH, '//form[@class="bb-password-recovery-form"]')
    GOOGLE_BUTTON = (By.CLASS_NAME, 'bb-button.e-service-button.m-color-tertiary.m-size-default')


class HomePageLocators:
    USER_AVATAR = (By.CLASS_NAME, '//a[@class="bb-avatar"]')
