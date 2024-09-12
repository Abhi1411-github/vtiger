
from auto import Demo

class LoginPage:

    locators = { "user_name" : ("xpath","//input[@name='user_name']"),
                 "password" : ("xpath","//input[@name='user_password']")
                 }

    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):
        s = Demo(self.driver)
        s.text_fill(LoginPage.locators["user_name"], value=username)
        s.text_fill(LoginPage.locators["password"],value=password)
        s.click_button(("xpath","//input[@id='submitButton']"))





