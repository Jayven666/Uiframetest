import os
import sys
import time
import unittest

from report import HTMLTestRunner

# 获取当前py文件路径地址，并进行路径分割（分割成目录路径和文件名称）
# dirname=D:\JavaDevelop\PycharmProjects\Uiframe0test filename=testrunner.py
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
print(dirname, filename)
case_path = ".\\case\\web\\"
result = dirname + "\\report\\"


def Creatsuite():
    # 定义单元测试用例集
    # TestSuite()是python中的一个测试套件，实例化测试套件
    testunit = unittest.TestSuite()

    # 搜索用例文件的方法
    # pattern：正则匹配；defaultTestLoader.discover方法自动根据测试目录查找py文件；discover就能拿到web目录下所有的py文件
    discover = unittest.defaultTestLoader.discover(case_path, pattern='*.py', top_level_dir=None)

    # 将测试用例加入测试套件中
    # 内层循环addTest()，把py文件中的test方法全部加载到测试套件里，这样就能获取所有py文件中的test方法
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
        # print testunit
    return testunit


test_case = Creatsuite()

# 获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# 定义个报告存放路径，支持相对路径
tdresult = result + day

if os.path.exists(tdresult):  # 检验文件夹路径是否已经存在
    filename = tdresult + "\\" + now + "_result.html"
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='测试报告',
                                           description='执行情况：')

    # 运行测试用例
    runner.run(test_case)
    fp.close()  # 关闭报告文件
else:
    os.mkdir(tdresult)  # 创建测试报告文件夹
    filename = tdresult + "\\" + now + "_result.html"
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='Selenium测试报告',
                                           description='执行情况：')

    # 运行测试用例
    runner.run(test_case)
    fp.close()  # 关闭报告文件
