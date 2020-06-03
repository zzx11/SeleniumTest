import time

from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.logger import Logger
from common.poium import Page, PageElement

my_log = Logger(logger='SettingPage').get_log()


class SettingPage(Page):
    setting_btn = PageElement(xpath="//*[@id='container']/div[1]/ul/li[5]/a", describe="setting_btn")
    create__btn = PageElement(xpath="//*[@id='container']/div[2]/div[2]/div/div[2]/div/div[3]/div[1]/button[1]",
                              describe="create__btn")
    project_name_input = PageElement(
        xpath="//*[@id='container']/div[2]/div[2]/div/div[2]/div/div[6]/div/div[2]/div[1]/input", describe="project_name_input")
    project_path_input = PageElement(
        xpath="//*[@id='container']/div[2]/div[2]/div/div[2]/div/div[6]/div/div[2]/div[2]/input", describe="project_path_input")
    save_btn = PageElement(xpath="//*[@id='container']/div[2]/div[2]/div/div[2]/div/div[6]/div/div[3]/button[2]",
                           describe="save_btn")
    path = "E:\JavaProject\dcksh_test\files\data\ModelTest1"

    def create_project(self):
        my_log.info("start create project!")
        time.sleep(2)
        self.setting_btn.click()
        self.get("http://localhost:8080/dcksh/system.html#/setting/project")
        time.sleep(2)
        self.create__btn.click()
        time.sleep(2)
        self.project_name_input.send_keys("自动化测试")
        self.project_path_input.send_keys(self.path)
        time.sleep(2)
        self.save_btn.click()
        time.sleep(2)
