from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")

    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")



class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    EXPECTED_BASKET_ELEMENT = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    REAL_BASKET_ELEMENT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs > div > h2")
