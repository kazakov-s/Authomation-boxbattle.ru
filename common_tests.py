from pages.login_page import LoginPage
from pages.urls import REGISTER_URL
from time import sleep


class TestAuthorizationForm_Basic_Functionality:

    def test_authorization_with_valid_data(self, browser):
        link = REGISTER_URL
        page = LoginPage(browser, link)
        page.open()
        page.should_be_non_authorized_user()
        page.register_new_user('dr.neologic@yandex.ru', 'Wcppos321')
        sleep(1)
