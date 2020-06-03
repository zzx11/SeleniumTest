import unittest
from config.browser_engine import BrowserEngine
from page.login_page import LoginPage
from page.setting_page import SettingPage


class Setting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserEngine().init_driver()
        po = LoginPage(cls.driver)
        po.get("http://localhost:8080/dcksh/index.html")
        po.login()
        cls.driver.implicitly_wait(30)

    def test_create_project(self):
        """
        测试新增项目
        """
        po = SettingPage(self.driver)
        po.create_project()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
