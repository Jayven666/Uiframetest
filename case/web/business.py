# coding=utf-8
from selenium import webdriver
import unittest
import os
import time
from public.login import Mylogin

class TestBusiness(unittest.TestCase):
    # setUp一般用来做初始化
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://101.133.169.100:8088/index.html#/login")
        self.driver.maximize_window()
        time.sleep(5)
        # 记录这条用例开始执行的时间：2021-05-19-14-55-20
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    # tearDown一般进行释放和清理操作
    def tearDown(self):
        filedir = "D:/软件测试/day21_5.16/screenshot/"
        # 如果路径不存在就创建目录
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', '软件测试', 'day21_5.16', 'screenshot'))
        # 记录这条用例结束执行的时间：2021-05-19-14-55-20
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        # 截图的意义：tearDown是最后执行所以截图的页面也是最后的页面，截图名称为：文件路径+结束时间.png
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def test_shangye03_01(self):
        """验证商业智能-销售漏斗筛选下拉框默认文本"""
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(15)
        # 点击商业智能
        self.driver.find_element_by_xpath('//div[text()="商业智能"]').click()
        # 点击销售漏斗分析
        self.driver.find_element_by_xpath('//ul[@role="menubar"]/li[2]/div').click()
        time.sleep(2)
        # 点击销售漏斗
        self.driver.find_element_by_xpath('//div[@id="app"]/section/section/aside/div/ul/li[2]/ul/a[1]/li').click()
        time.sleep(2)
        # 获取下拉框的默认属性值
        timeFrame = self.driver.find_element_by_xpath('//input[@placeholder="请选择选择"]').get_attribute('value')
        print("timeFrame:"+timeFrame)
        # 比较
        self.assertEqual("本年", timeFrame)

    def test_shangye03_02(self):
        """验证部门选择下拉框的默认文本显示是否正常"""
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(15)
        # 点击商业智能
        self.driver.find_element_by_xpath('//div[text()="商业智能"]').click()
        # 点击销售漏斗分析
        self.driver.find_element_by_xpath('//ul[@role="menubar"]/li[2]/div').click()
        time.sleep(2)
        # 点击销售漏斗
        self.driver.find_element_by_xpath('//div[@id="app"]/section/section/aside/div/ul/li[2]/ul/a[1]/li').click()
        time.sleep(2)
        # 获取下拉框的默认属性值
        dpFrame = self.driver.find_element_by_xpath('//input[@placeholder="选择部门"]').get_attribute('value')
        print("dpFrame:"+dpFrame)
        # 比较
        self.assertEqual("办公室", dpFrame)

if __name__ == "__main__":
    unittest.main()
