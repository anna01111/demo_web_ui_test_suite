from main.base_element import BaseElement
from selenium.webdriver.common.by import By
from main.base_page import BasePage


class RegisterPopup(BasePage):

    @property
    def username_field(self):
        locator = (By.XPATH, '//*[@id="register-username-modal"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def first_name_field(self):
        locator = (By.XPATH, '//*[@id="register-first-modal"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def last_name_field(self):
        locator = (By.XPATH, '//*[@id="register-last-modal"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def email_field(self):
        locator = (By.XPATH, '//*[@id="register-email-modal"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def password_field(self):
        locator = (By.XPATH, '//*[@id="register-password-modal"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def register_button(self):
        locator = (By.XPATH, '//*[@onclick="return register()"]')
        return BaseElement(driver=self.driver, locator=locator)
