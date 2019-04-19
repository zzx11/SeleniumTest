import time

from selenium.webdriver.common.by import By
from Common.base_page import BasePage
from Common.logger import Logger

my_log = Logger(logger='SettingPage').get_log()


class SettingPage(BasePage):
    setting_btn = (By.XPATH, "//*[@id='container']/div[1]/ul/li[5]/a")
    create__btn = (By.XPATH, "//*[@id='container']/div[2]/div[2]/div/div[2]/div/div[3]/div[1]/button[1]")
    project_name_input = (By.XPATH, "//*[@id='container']/div[2]/div[2]/div/div[2]/div/div[6]/div/div[2]/div[1]/input")
    project_path_input = (By.XPATH, "//*[@id='container']/div[2]/div[2]/div/div[2]/div/div[6]/div/div[2]/div[2]/input")
    save_btn = (By.XPATH, "//*[@id='container']/div[2]/div[2]/div/div[2]/div/div[6]/div/div[3]/button[2]")
    path = "E:\JavaProject\dcksh_test\files\data\ModelTest1"

    def create_project(self):
        my_log.info("start create project!")
        time.sleep(2)
        self.click(self.setting_btn)
        self.get_url("http://localhost:8080/dcksh/system.html#/setting/project")
        time.sleep(2)
        self.click(self.create__btn)
        time.sleep(2)
        self.input(self.project_name_input, "自动化测试")
        self.input(self.project_path_input, self.path)
        time.sleep(2)
        self.click(self.save_btn)
        time.sleep(2)

