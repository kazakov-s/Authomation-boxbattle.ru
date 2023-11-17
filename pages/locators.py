from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_AVATAR = (By.PARTIAL_LINK_TEXT, 'avatar')

class LoginPageLocators:
    EMAIL = (By.XPATH, '//input[@type="text"]')
    PASSWORD = (By.XPATH, '//input[@type="password"]')
    BUTTON_SUBMIT = (By.XPATH, '//button[@type="submit"]')
    RECOVER_LINK = (By.XPATH, '//button[@class="e-recovery-button"]')
    RECOVER_TITLE = (By.XPATH, '//form[@class="bb-password-recovery-form"]')
    GOOGLE_BUTTON = (By.XPATH, '//ul/li[1]/button')
    MICROSOFT_BUTTON = (By.XPATH, '//ul/li[2]/button')
    VKONTAKTE_BUTTON = (By.XPATH, '//ul/li[3]/button')
    APPLEID_BUTTON = (By.XPATH, '//ul/li[4]/button')
    EN_BUTTON = (By.XPATH, '//p[@id="en-US"]')
    SIGNIN_SPAN = (By.CLASS_NAME, 'bb-text.text-head-32-40.color-on-surface-88')


class HomePageLocators:
    USER_AVATAR = (By.CLASS_NAME, '//a[@class="bb-avatar"]')
