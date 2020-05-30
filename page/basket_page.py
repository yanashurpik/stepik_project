from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_not_be_items(self):

        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), "Basket is not empty"

    def should_be_empty_basket(self):

        real_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        assert real_text == "Your basket is empty. Continue shopping", "Basket should be empty"