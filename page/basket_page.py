from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_not_be_items(self):

        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), "Basket is not empty"

    def should_be_empty_basket(self):

        real_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        assert real_text == "Ваша корзина пуста Продолжить покупки", "Basket should be empty"


    #Ожидаем, что в корзине нет товаров
    #Ожидаем, что есть текст о том что корзина пуста