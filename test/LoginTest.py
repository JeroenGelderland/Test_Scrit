from selenium.webdriver.common.action_chains import ActionChains
from test.TestClass import TestClass
from selenium.webdriver.common.keys import Keys
import time

class LoginTest(TestClass):
    def __init__(self, driver, name="Login"):
        super().__init__(driver, name)

    def run(self):
        self.driver.get("http://localhost:8000/")
        self.tests["login"] = self.login()
        super().run()

    def login(self):
        link = self.driver.find_element_by_css_selector('ul.login_search li a')
        link.click()
        time.sleep(3)
        emailInput = self.driver.find_element_by_id('email')
        emailInput.send_keys('pascal@gmail.com')

        passwordInput = self.driver.find_element_by_id('password')
        passwordInput.send_keys('weerbaarBrabant')

        submit = self.driver.find_element_by_css_selector('button')
        submit.click()
        time.sleep(3)
        expectedURL = 'http://localhost:8000/home'
        currentURL =  self.driver.current_url
        print(expectedURL)
        print(currentURL)
        return expectedURL == currentURL