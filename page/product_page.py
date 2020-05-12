from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

        self.solve_quiz_and_get_code()

        expected_element = self.browser.find_element(*ProductPageLocators.EXPECTED_BASKET_ELEMENT).text
        real_element = self.browser.find_element(*ProductPageLocators.REAL_BASKET_ELEMENT).text
        assert expected_element == real_element, "PRODUCT IS NOT IN BASKET"





