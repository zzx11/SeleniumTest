from time import sleep
from common.firefox.test_firefox import myfox


def highLightElement(driver, element):
    # 封装好的高亮显示页面元素的方法
    # 使用JavaScript代码将传入的页面元素对象的背景颜色和边框颜色分别
    # 设置为绿色和红色
    driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                          element, "background:green ;border:2px solid red;")


browser = myfox().work()
# browser.maximize_window()
browser.get("http://192.168.3.145:10001/aaf/index")
print(browser.title)
showAllBtn = browser.find_element_by_xpath("//*/div[contains(text(), '展示全部')]")
# 调用高亮显示的元素封装函数
highLightElement(browser, showAllBtn)
showAllBtn.click()
# 菜单栏iframe跳转进入
browser.switch_to.frame(browser.find_element_by_xpath('//iframe[ @id= "redirectUri"]'))
sleep(1)
jydj = browser.find_element_by_xpath('//span[ @title= "简易登记"]')
highLightElement(browser, jydj)
sleep(1)
jydj.click()
# topIcisMainFrame跳转进入
browser.switch_to.frame(browser.find_element_by_id('topIcisMainFrame'))
sleep(1)
# 不核名按钮，核名按钮value=1
browser.find_element_by_xpath('//input[ @name= "veriNameFlag" and @value=0]').click()
# 增加按钮
browser.find_element_by_id('addSimInvButton').click()


# sumbitButton = browser.find_element_by_id("stb")
# # 调用高亮显示的封装函数，将搜索按钮进行高亮显示
# highLightElement(browser, sumbitButton)
# sleep(3)
# sumbitButton.click()
# sleep(3)
