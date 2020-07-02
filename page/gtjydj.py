from time import sleep

from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.poium import Page, PageElement


class GTJYDJPage(BasePage):
    # 核名1，不核名0
    veriNameFlag1_btn = "xpath=>//*[@name='veriNameFlag' and @value=1]"
    veriNameFlag0_btn = "xpath=>//*[@name='veriNameFlag' and @value=0]"
    add_btn = "id=>addSimInvButton"
    legalName_input = "xpath=>//*[@name='mainBodyDto.legalCommissarial']"
    topIcisMain_frame = "xpath=>//iframe[ @id= 'topIcisMainFrame']"
    cardNum_input = "xpath=>//*[@name='legalDto.certificateCode']"
    onlineBusiFlag1_btn = "xpath=>//*[@name='addressDto.onlineBusiFlag' and @value=1]"
    onlineBusiFlag0_btn = "xpath=>//*[@name='addressDto.onlineBusiFlag' and @value=0]"
    address_input = "xpath=>//input[@id='townCode']/../span"  # 经营场所输入框
    district = "xpath=>//a[@data-count='district']"  # 区县
    district_de = "xpath=>//a[@data-code='522701']"  # 都匀市
    county = "xpath=>//a[@data-count='county']"  # 街道
    county_de = "xpath=>//a[@data-code='522701004']"  # 小围寨街道
    addressDe_input = "xpath=>//*[@name='mainBodyAddiInfo.addInfo']"

    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)

    def no_name(self):
        print("选择不核名，新增简易登记申请")
        self.switch_to_frame1(self.topIcisMain_frame)
        sleep(3)
        self.click(self.veriNameFlag0_btn)
        sleep(3)
        self.click(self.add_btn)
        sleep(3)
        self.input(self.legalName_input, '安初坚')
        self.input(self.cardNum_input, '411727197001217656')
        self.click(self.onlineBusiFlag0_btn)
        self.click(self.address_input)
        self.click(self.district)
        self.click(self.district_de)
        self.click(self.county)
        self.click(self.county_de)
