from .page.product_page import ProductPage
from .page.basket_page import BasketPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.login
class TestLoginFromProductPage:

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        page.should_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


@pytest.mark.add_to_basket
class TestAddToBasketFromProductPage:

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.basket
class TestBasketFromProductPage:

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()

        page.go_to_basket_from_every_page()
        basket_page = BasketPage(browser, browser.current_url)
        time.sleep(5)
        basket_page.should_not_be_items()
        basket_page.should_be_empty_basket()


@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage:

    def test_user_is_authorized(self, setup, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, setup, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, setup, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()