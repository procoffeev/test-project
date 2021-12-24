from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By



class ProductPage(BasePage):
    def product_add_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM), "The add to cart button was not found"
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM).click()
                        
                   
    def should_be_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE), "Price product not found"
        assert self.browser.find_element(*ProductPageLocators.MSG_PRICE), "Message price not found"
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        print()
        print(price)
        msg_price = self.browser.find_element(*ProductPageLocators.MSG_PRICE).text
        print()
        print(msg_price)
        assert price == msg_price, "The price of the added product does not match"
        
        
    def should_be_name_product(self):
        assert self.browser.find_element(*ProductPageLocators.NAME), "Name product not found"
        assert self.browser.find_element(*ProductPageLocators.MSG_NAME_PRODUCT), "Message name product not found"
        name = self.browser.find_element(*ProductPageLocators.NAME).text
        print()
        print(name)
        msg_name = self.browser.find_element(*ProductPageLocators.MSG_NAME_PRODUCT).text
        print()
        print(msg_name)
        assert name == msg_name, "The name of the added product does not match"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"
        
       
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is disappear"

        
