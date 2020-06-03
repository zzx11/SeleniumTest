import unittest
import time
from config.browser_engine import BrowserEngine
from page.login_page import LoginPage


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = BrowserEngine().init_driver()
        self.driver.implicitly_wait(30)

    def test_login(self):
        """
        测试用户登录
        """
        po = LoginPage(self.driver)
        po.get("http://localhost:8080/dcksh/index.html")
        po.input_username("admin")
        po.input_pwd("admin")
        po.click_login_btn()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()




