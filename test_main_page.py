from .page.main_page import MainPage
from .page.login_page import LoginPage
from .page.basket_page import BasketPage
import pytest
import time


@pytest.mark.login
class TestLoginFromMainPAge:

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()

        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_form()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.basket
class TestBasketFromMainPage:

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()

        page.go_to_basket_from_every_page()
        basket_page = BasketPage(browser, browser.current_url)
        time.sleep(5)
        basket_page.should_not_be_items()
        basket_page.should_be_empty_basket()
