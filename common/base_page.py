from selenium.common.exceptions import NoSuchElementException, TimeoutException
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

    def find_element(self, selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
        submit_btn = "id=>su"
        login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
        如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                my_log.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                my_log.error("NoSuchElementException: %s" % e)
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                my_log.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                my_log.error("NoSuchElementException: %s" % e)
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def find_element_by_xpath(self, xpath_str):
        try:
            element = self.driver.find_element_by_xpath(xpath_str)
            my_log.info("Had find the element \' %s \' successful "
                        "by xpath via value: %s " % (element.text, xpath_str))
            return element
        except NoSuchElementException as e:
            my_log.error("NoSuchElementException: %s" % e)

    def _init_wait(self, timeout):
        if timeout is None:
            return WebDriverWait(driver=self.driver, timeout=config.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self.driver, timeout=timeout)

    def input(self, locator, text):
        ele = self.find_element(locator)
        ele.send_keys(text)

    def click(self, selector):
        ele = self.find_element(selector)
        ele.click()

    def switch_to_frame1(self, selector):
        # self.driver.switch_to_frame(self.driver.find_element_by_xpath("//iframe[ @id= 'redirectUri']"))
        frame = self.find_element(selector)
        self.driver.switch_to_frame(frame)
        # self.driver.switch_to.default_content()

    def input2(self, ele, text):
        ele.send_keys(text)

    def click2(self, xpath_str):
        element = self.find_element_by_xpath(xpath_str)
        element.click()
