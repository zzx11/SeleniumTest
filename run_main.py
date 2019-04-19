import time
from Common.HTMLTestRunner_PY3 import HTMLTestRunner
from unittest import defaultTestLoader
from Common.utx import *

# 指定测试用例目录
test_dir = './TestCase'
test_suits = defaultTestLoader.discover(test_dir, pattern='seting_test.py')

if __name__ == "__main__":
    setting.check_case_doc = False  # 关闭检测是否编写了测试用例描述
    setting.full_case_name = True
    setting.sort_case = True  # 是否按照编写顺序，对用例进行排序

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './Report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='WebUI自动化测试报告',
                            description='运行环境：Windows7, Python3.6, MySQL5.6 ')
    runner.run(test_suits)
    fp.close()
