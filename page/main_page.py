from .base_page import BasePage
from .locators import MainPageLocators
# from .login_page import LoginPage 1 способ перехода на ссыдку


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
