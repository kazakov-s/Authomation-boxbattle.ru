from pages.login_page import LoginPage
from pages.urls import REGISTER_URL
from time import sleep


#Общий функционал (позитивные и негативные тесты)
class TestAuthorizationForm_Basic_Functionality:

# #Тест №1. Проверка работы формы с валидными данными (e-mail и пароль)
#     def test_authorization_with_valid_data(self, browser):
#         link = REGISTER_URL
#         page = LoginPage(browser, link)
#         page.open()
#         page.should_be_non_authorized_user()
#         page.register_new_user('dr.neologic@yandex.ru', 'Wcppos321')
#         sleep(1)
#
# #Тест №2. Проверка ссылки "Восстановить пароль"
#     def test_recover_password_link(self, browser):
#         link = REGISTER_URL
#         page = LoginPage(browser, link)
#         page.open()
#         page.should_be_non_authorized_user()
#         page.should_be_password_recover_link()

#Тест №3. Авторизация через аккаунт Google
    def test_google_account_authorization(self, browser):
        link = REGISTER_URL
        page = LoginPage(browser, link)
        page.open()
        page.should_be_non_authorized_user()
        page.google_account_authorization()
