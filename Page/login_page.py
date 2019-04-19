from selenium.webdriver.common.by import By
from Common.base_page import BasePage


class LoginPage(BasePage):
    username_input = (By.XPATH, "//*[@id='container']/div[1]/div/div[1]/input")
    password_input = (By.XPATH, "//*[@id='container']/div[1]/div/div[2]/input")
    login_btn = (By.XPATH, "//*[@id='container']/div[1]/div/button")

    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)

    def login(self):
        self.input(self.username_input, text="admin")
        self.input(self.password_input, text="123456")
        self.click(self.login_btn)

    def input_username(self, username):
        print("输入用户名")
        self.input(self.username_input, text=username)

    def input_pwd(self, password):
        print("输入密码")
        self.input(self.password_input, text=password)

    def click_login_btn(self):
        print("点击登录")
        self.click(self.login_btn)
