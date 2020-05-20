from .page.main_page import MainPage
from .page.login_page import LoginPage
from .page.basket_page import BasketPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    # page.should_be_login_link()
    # login_page = page.go_to_login_page()  # 1 способ перехода поссылке

    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()

    page.go_to_basket_from_every_page()
    basket_page = BasketPage(browser, browser.current_url)
    time.sleep(5)
    # basket_page.should_not_be_items()
    basket_page.should_be_empty_basket()

