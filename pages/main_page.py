from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, LOGIN_LINK)
        login_link.click()
        
    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, LOGIN_LINK), "Login link is not presented"