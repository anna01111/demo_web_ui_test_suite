from main.base_element import BaseElement
from selenium.webdriver.common.by import By
from main.base_page import BasePage


class HomePage(BasePage):

    @property
    def url(self):
        return self.base_url

    @property
    def catalogue_button(self):
        locator = (By.CSS_SELECTOR, '#tabCatalogue a')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def basket_button(self):
        locator = (By.CSS_SELECTOR, '#basket-overview > a')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_button(self):
        locator = (By.CSS_SELECTOR, '#login > a')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_button_present_on_page(self):
        """
        return: bool
        """
        return self.driver.find_elements(By.CSS_SELECTOR, '#login > a')

    @property
    def account_button(self):
        locator = (By.CSS_SELECTOR, '#tabAccount > a')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def account_button_present_on_page(self):
        """
        return: bool
        """
        return self.driver.find_elements(By.CSS_SELECTOR, '#tabAccount > a')

    @property
    def logged_in_button(self):
        locator = (By.CSS_SELECTOR, '#howdy > a')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def logged_in_button_present_on_page(self):
        """
        return: bool
        """
        return self.driver.find_elements(By.CSS_SELECTOR, '#howdy > a')

    @property
    def logout_button(self):
        locator = (By.CSS_SELECTOR, '#logout > a')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def logout_button_present_on_page(self):
        """
        return: bool
        """
        return self.driver.find_elements(By.CSS_SELECTOR, '#logout > a')

    @property
    def register_button(self):
        locator = (By.CSS_SELECTOR, '#register > a')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def register_button_present_on_page(self):
        """
        return: bool
        """
        return self.driver.find_elements(By.CSS_SELECTOR, '#register > a')

    @property
    def product_image(self):
        locator = (By.CSS_SELECTOR, 'div.product img')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_name(self):
        locator = (By.CSS_SELECTOR, 'div.product div.text a')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_price(self):
        locator = (By.CSS_SELECTOR, 'div.product div.text p')
        return BaseElement(driver=self.driver, locator=locator)

