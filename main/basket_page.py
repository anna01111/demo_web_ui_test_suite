from main.base_element import BaseElement
from selenium.webdriver.common.by import By
from main.base_page import BasePage


class BasketPage(BasePage):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    @property
    def update_basket_button(self):
        locator = (By.CSS_SELECTOR, 'a[onclick="updateCart()"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def order_summary_total(self):
        locator = (By.ID, 'orderGrandTotal')
        '''
        The element is created twice to avoid selenium.common.exceptions.StaleElementReferenceException: 
        Message: stale element reference: element is not attached to the page document
        '''
        _ = BaseElement(driver=self.driver, locator=locator)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_name(self):
        locator = (By.CSS_SELECTOR, 'tr.item > td:nth-child(3) > a')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def unit_price(self):
        locator = (By.CSS_SELECTOR, 'tr.item > td:nth-child(5)')
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

    @property
    def remove_icon(self):
        locator = (By.CSS_SELECTOR, '#cart-list > tr > td:nth-child(8) > a > i')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_present_on_page(self):
        """
        return: bool
        """
        return self.driver.find_elements(By.CSS_SELECTOR, 'tr.item')
