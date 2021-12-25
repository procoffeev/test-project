from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_login = self.browser.find_element(*LoginPageLocators.REGISTER_INPUT)
        input_login.send_keys(email)
        input_pswd1 = self.browser.find_element(*LoginPageLocators.PSWD_1)
        input_pswd1.send_keys(password)
        input_pswd2 = self.browser.find_element(*LoginPageLocators.PSWD_2)
        input_pswd2.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_BUTTON_SUBMIT)
        button_submit.click()
        
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
         