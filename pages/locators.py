from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    
class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner .row")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    
class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    
class ProductPageLocators():
    MSG_NAME_PRODUCT = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    MSG_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    
