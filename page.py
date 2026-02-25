from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_input = (By.ID, "user-name")
        self.pass_input = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    def login(self, username, password):
        self.driver.find_element(*self.user_input).send_keys(username)
        self.driver.find_element(*self.pass_input).send_keys(password)
        self.driver.find_element(*self.login_btn).click()

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_btn = (By.CLASS_NAME, "btn_inventory")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_first_item(self):
        self.driver.find_elements(*self.add_btn)[0].click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text
