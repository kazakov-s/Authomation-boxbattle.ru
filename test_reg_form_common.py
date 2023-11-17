from pages.login_page import LoginPage
from pages.urls import REGISTER_URL
from time import sleep


#Общий функционал (позитивные и негативные тесты)
class TestAuthorizationForm_Basic_Functionality:

    URL = REGISTER_URL

# #Тест №1. Проверка работы формы с валидными данными (e-mail и пароль)
#     def test_authorization_with_valid_data(self, browser):
#         page = LoginPage(browser, REGISTER_URL)
#         page.open()
#         page.should_be_non_authorized_user()
#         page.register_new_user('dr.neologic@yandex.ru', 'Wcppos321')
#         sleep(1)
#
# #Тест №2. Проверка ссылки "Восстановить пароль"
#     def test_recover_password_link(self, browser):
#         page = LoginPage(browser, REGISTER_URL)
#         page.open()
#         page.should_be_non_authorized_user()
#         page.should_be_password_recover_link()
#
# #Тест №3. Авторизация через аккаунт Google
#     def test_google_account_authorization(self, browser):
#         page = LoginPage(browser, REGISTER_URL)
#         page.open()
#         page.should_be_non_authorized_user()
#         page.google_account_authorization()
#
#
# #Тест №4. Авторизация через аккаунт Microsoft
#     def test_microsoft_account_authorization(self, browser):
#         page = LoginPage(browser, REGISTER_URL)
#         page.open()
#         page.should_be_non_authorized_user()
#         page.microsoft_account_authorization()
#
#
# #Тест №5. Авторизация через аккаунт ВКонтакте
#     def test_vkontakte_account_authorization(self, browser):
#         page = LoginPage(browser, REGISTER_URL)
#         page.open()
#         page.should_be_non_authorized_user()
#         page.vkontakte_account_authorization()
#
#
# #Тест №6. Авторизация через аккаунт Apple ID
#     def test_appleid_account_authorization(self, browser):
#         page = LoginPage(browser, REGISTER_URL)
#         page.open()
#         page.should_be_non_authorized_user()
#         page.appleid_account_authorization()
#
#
# #Тест №7. Авторизация через аккаунт Apple ID
#     def test_should_switch_to_english(self, browser):
#         page = LoginPage(browser, REGISTER_URL)
#         page.open()
#         page.should_be_non_authorized_user()
#         page.should_switch_to_english()
#         sleep(5)