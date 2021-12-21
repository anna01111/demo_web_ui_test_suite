from main.base_element import BaseElement
from selenium.webdriver.common.by import By
from main.base_page import BasePage


class ProductPage(BasePage):

    @property
    def product_name(self):
        locator = (By.CSS_SELECTOR, 'div.box h1')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_price(self):
        locator = (By.CSS_SELECTOR, 'div.box p#price')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_to_card_button(self):
        locator = (By.CSS_SELECTOR, 'a[id=buttonCart]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def basket_button(self):
        locator = (By.XPATH, '//*[@id="numItemsInCart"]')
        '''
        The element is created twice to avoid selenium.common.exceptions.StaleElementReferenceException: 
        Message: stale element reference: element is not attached to the page document
        '''
        _ = BaseElement(driver=self.driver, locator=locator)
        return BaseElement(driver=self.driver, locator=locator)
