from selenium.webdriver.common.by import By
from Common.base_page import BasePage
from Common.poium import Page, PageElement


class LoginPage(Page):
    username_input = PageElement(xpath="//*[@id='container']/div[1]/div/div[1]/input", describe="用户名输入框")
    password_input = PageElement(xpath="//*[@id='container']/div[1]/div/div[2]/input", describe="密码输入框")
    login_btn = PageElement(xpath="//*[@id='container']/div[1]/div/button", describe="登录按钮")

    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)

    def login(self):
        # self.input(self.username_input, text="admin")
        # self.input(self.password_input, text="123456")
        # self.click(self.login_btn)
        self.username_input.send_keys("admin")
        self.password_input.send_keys("123456")
        self.login_btn.click()

    def input_username(self, username):
        print("输入用户名")
        self.username_input.send_keys(username)

    def input_pwd(self, password):
        print("输入密码")
        self.password_input.send_keys(password)

    def click_login_btn(self):
        print("点击登录")
        self.login_btn.click()
