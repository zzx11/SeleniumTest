from common.firefox.test_firefox import myfox

driver = myfox().work()
js = 'window.open("http://192.168.3.145:10002/auth/login")'
driver.execute_script(js)