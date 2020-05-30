from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)

    def go_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

        expected_element = self.browser.find_element(*ProductPageLocators.EXPECTED_BASKET_ELEMENT).text
        real_element = self.browser.find_element(*ProductPageLocators.REAL_BASKET_ELEMENT).text
        assert expected_element == real_element, "PRODUCT IS NOT IN BASKET"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.REAL_BASKET_ELEMENT), \
            "Success message is presented, but should not be"
        #is_not_element_present: упадет, как только увидит
        # искомый элемент. Не появился: успех, тест зеленый.

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.REAL_BASKET_ELEMENT), \
            "Success message is presented, but should disappear"
        #is_disappeared: будет ждать до тех пор, пока элемент не исчезнет.

