from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.logger import Logger
from config import config
my_log = Logger(logger='BasePage').get_log()


class BasePage(object):

    def __init__(self, driver, parent=None):
        self.driver = driver
        self.timeout = 30
        self.parent = parent

    def get_url(self, url):
        my_log.info("open url : %s " % url)
        self.driver.get(url)

    def find_element(self, *locator, timeout=None):
        try:
            return self._init_wait(timeout).until(EC.visibility_of_element_located(locator=locator))
        except (NoSuchElementException, TimeoutException):
            self.driver.quit()
            raise TimeoutException(msg='寻找元素失败, 定位方式为: {}'.format(locator))

    def _init_wait(self, timeout):
        if timeout is None:
            return WebDriverWait(driver=self.driver, timeout=config.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self.driver, timeout=timeout)

    def input(self, locator, text):
        ele = self.find_element(*locator)
        ele.send_keys(text)

    def click(self, locator):
        ele = self.find_element(*locator)
        ele.click()

    def input2(self, ele, text):
        ele.send_keys(text)

    def click2(self, ele):
        ele.click()
