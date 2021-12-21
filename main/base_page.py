class BasePage:
    base_url = 'http://127.0.0.1/'
    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)
        return None

    def switch_to_pop_up(self):
        _ = self.driver.switch_to.active_element
        return None


"""
    def switch_back_to_page(self):
        self.driver.switch_to.default_content()
        return None

"""
