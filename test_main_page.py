from .page.main_page import MainPage
from .page.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    # page.should_be_login_link()
    # login_page = page.go_to_login_page()  # 1 способ перехода поссылке

    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()