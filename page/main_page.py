from time import sleep

from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.poium import Page, PageElement


class MainPage(Page):
    message_btn = PageElement(xpath="//*[@id='notificationMessageOperate']/img[1]", describe="消息组件按钮")
    showAllBtn = PageElement(xpath="//*/div[contains(text(), '展示全部')]", describe="主页展示全部按钮")
    # login_btn = PageElement(xpath="//*[@id='container']/div[1]/div/button", describe="登录按钮")

    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)

    def show_all(self):
        print("关闭消息组件，点击展示全部，跳转市场主体登记")
        sleep(3)
        self.message_btn.click()
        sleep(3)
        self.showAllBtn.click()
