from time import sleep

from common.base_page import BasePage


class MainPage(BasePage):
    message_btn = "xpath=>//*[@id='notificationMessageOperate']/img[1]"
    showAllBtn = "xpath=>//*/div[contains(text(), '展示全部')]"
    scztdj_btn = "xpath=>//*/span[contains(string(), '市场主体登记')]/text()/.."
    gtjydj_btn = "xpath=>//*/span[@title='简易登记']"
    redirectUri_iframe = "xpath=>//iframe[ @id= 'redirectUri']"

    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)

    def show_all(self):
        print("关闭消息组件，点击展示全部，跳转市场主体登记")
        sleep(3)
        # self.click(self.message_btn)
        # sleep(3)
        self.click(self.showAllBtn)
        sleep(3)
        self.switch_to_frame1(self.redirectUri_iframe)
        sleep(3)
        self.click(self.scztdj_btn)

    def click_gtjydj_menu(self):
        print("跳转个体简易登记页面")
        self.click(self.gtjydj_btn)


