from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Product in basket"
    
    def should_be_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Basket is not empty"
        
    def should_not_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Basket is empty"
        