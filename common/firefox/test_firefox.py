import pickle, psutil, win32api, logging
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from common.firefox import myFirefox
import project_path

path = project_path.path
driver_path = path + '\\tools\\geckodriver.exe'
data_path = path + '\\data\\params.data'


class myfox():
    '''目的：不需要每次都重新打开浏览器'''

    def __init__(self):
        self.file = data_path
        self.gecko = driver_path
        self.url = "http://127.0.0.1:4444"
        self.capabilities = DesiredCapabilities.FIREFOX  # 实际就是选定firefox浏览器

    def creatfirefox(self):
        '''先运行geckodriver，启动浏览器，记录ID跟URL，返回driver'''
        win32api.ShellExecute(0, 'open', self.gecko, '', '', 0)  # 先在后台运行geckodriver
        driver = webdriver.remote.webdriver.WebDriver(command_executor=self.url,
                                                      desired_capabilities=self.capabilities,
                                                      )
        params = {}
        params["session_id"] = driver.session_id
        params["server_url"] = driver.command_executor._url
        with open(self.file, 'wb') as f:
            pickle.dump(params, f)
        return driver

    def work(self):
        '''先判断geckodriver启动没有，没启动就直接运行，启动了先try，不行就删除geckodriver，再次运行friefox'''
        p_name = [psutil.Process(i).name() for i in psutil.pids()]  # 罗列进程的程序，如果gecko没有，直接创建启动
        if 'geckodriver.exe' not in p_name:
            driver = self.creatfirefox()
        else:
            try:  # 已经有gecko了，试试能不能在旧的浏览器上执行myfirefox(有可能对应的浏览器已经关闭了)
                with open(self.file, 'rb') as f:
                    params = pickle.load(f)
                driver = myFirefox.myWebDriver(service_url=params["server_url"], session_id=params["session_id"])
                driver.refresh()
            except Exception as e:
                # 当不能直接在旧浏览器上操作时，那就删了gecko重新再运行
                logging.error('浏览器跟geckodriver不对应！！\n%s' % e)
                [p.kill() for p in psutil.process_iter() if p.name() == 'geckodriver.exe']
                # os.system("taskkill /F /IM geckodriver.exe") 这种方法会有乱码！！
                driver = self.creatfirefox()
        return driver

# driver = myfox().work()
# driver.get('https://www.baidu.com/')
