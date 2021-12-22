from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
         
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM_LINK), "Login form is not presented"
         
    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_REGISTER_FORM), "Registration form is not presented"
        time.sleep(11)
         