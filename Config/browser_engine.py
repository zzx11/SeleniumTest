from selenium import webdriver

from Config import config


class BrowserEngine(object):
    driver_file_path = ""
    CHROME_DRIVER = ""
    FIREFOX_DRIVER = ""
    IE_DRIVER = ""

    def __init__(self, browser=None):
        if browser is None:
            self._browser_type = config.DEFAULT_BROWSER
        else:
            self._browser_type = browser
        self._driver = None

    def init_driver(self):
        if self._browser_type.lower() == 'chrome':
            # self._driver = webdriver.Chrome(executable_path=self.CHROME_DRIVER) # 指定驱动文件位置
            self._driver = webdriver.Chrome()
        elif self._browser_type.lower() == 'firefox':
            self._driver = webdriver.Firefox(executable_path=self.FIREFOX_DRIVER)
        elif self._browser_type.lower() == 'ie':
            self._driver = webdriver.Ie(executable_path=self.IE_DRIVER)
        else:
            ValueError('传入的浏览器类型错误,目前仅支持Chrome/Firefox/IE.')
        self._driver.implicitly_wait(time_to_wait=config.UI_WAIT_TIME)
        return self._driver
