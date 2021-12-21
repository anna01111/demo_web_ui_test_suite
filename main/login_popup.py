
from main.base_element import BaseElement
from selenium.webdriver.common.by import By
from main.base_page import BasePage


class LoginPopup(BasePage):

    @property
    def username_field(self):
        locator = (By.ID, 'username-modal')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def password_field(self):
        locator = (By.ID, 'password-modal')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_button(self):
        locator = (By.CSS_SELECTOR, 'button[onclick="return login()"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_message(self):
        locator = (By.CSS_SELECTOR, '#login-message > div')
        return BaseElement(driver=self.driver, locator=locator)
