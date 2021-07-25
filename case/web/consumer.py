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

    def test_kehu04_01(self):
        """验证快速创建线索功能是否正常"""
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(30)
        # 点击进入客户管理
        self.driver.find_element_by_xpath('//div[text()="客户管理"]').click()
        time.sleep(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“线索”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[1]/span').click()
        time.sleep(2)
        # 点击并输入线索名称
        self.driver.find_element_by_xpath('//form/div[1]/div/div[1]/input').click()
        self.driver.find_element_by_xpath('//form/div[1]/div/div[1]/input').send_keys("高价回收矿卡")
        # 保存
        self.driver.find_element_by_xpath('//button[@class="el-button handle-button el-button--primary"]/span').click()
        time.sleep(2)
        # 点击进入线索列表
        self.driver.find_element_by_xpath('//li/span[text()="线索"]').click()
        time.sleep(2)
        # 查看是否有该条线索
        text = self.driver.find_element_by_xpath('//*[@id="crm-table"]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div').text
        print("text:"+text)
        self.assertEqual(text, "高价回收矿卡")

    def test_kehu04_02(self):
        """验证搜索线索功能是否正常"""
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(30)
        # 点击进入客户管理
        self.driver.find_element_by_xpath('//div[text()="客户管理"]').click()
        time.sleep(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“线索”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[1]/span').click()
        time.sleep(2)
        # 点击并输入线索名称
        self.driver.find_element_by_xpath('//form/div[1]/div/div[1]/input').click()
        self.driver.find_element_by_xpath('//form/div[1]/div/div[1]/input').send_keys("卖烧饼")
        # 保存
        self.driver.find_element_by_xpath('//button[@class="el-button handle-button el-button--primary"]/span').click()
        time.sleep(2)
        # 点击进入线索列表
        self.driver.find_element_by_xpath('//li/span[text()="线索"]').click()
        time.sleep(2)
        # 点击搜索框，输入一个字进行匹配
        self.driver.find_element_by_xpath('//input[@placeholder="请输入线索名称/手机/电话"]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="请输入线索名称/手机/电话"]').send_keys("卖")
        # 检查搜索结果中的线索名称是否包含搜索的字符
        self.assertIn("卖", self.driver.find_element_by_xpath('//*[@id="crm-table"]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div').text)

    def test_kehu04_03(self):
        """验证筛选线索功能是否正常"""
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(30)
        # 点击进入客户管理
        self.driver.find_element_by_xpath('//div[text()="客户管理"]').click()
        time.sleep(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“线索”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[1]/span').click()
        time.sleep(2)
        # 点击并输入线索名称
        self.driver.find_element_by_xpath('//form/div[1]/div/div[1]/input').click()
        self.driver.find_element_by_xpath('//form/div[1]/div/div[1]/input').send_keys("做直播")
        # 保存
        self.driver.find_element_by_xpath('//button[@class="el-button handle-button el-button--primary"]/span').click()
        time.sleep(2)
        # 点击进入线索列表
        self.driver.find_element_by_xpath('//li/span[text()="线索"]').click()
        time.sleep(2)
        # 点击高级筛选按钮
        self.driver.find_element_by_xpath('//div[text()="高级筛选"]').click()
        # 定位条件框，选择线索名称
        self.driver.find_element_by_xpath('//input[@placeholder="请选择要筛选的字段名"]').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span').click()
        self.driver.find_element_by_xpath('//input[@placeholder="请输入筛选条件"]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="请输入筛选条件"]').send_keys("做直播")
        # 确定
        self.driver.find_element_by_xpath('//*[@id="crm-main-container"]/div/div/div[2]/div[1]/div[1]/div[3]/div/div[3]/div/button[2]').click()
        # 检查搜索结果中的线索名称是否为筛选的条件
        self.assertEqual("做直播", self.driver.find_element_by_xpath(
            '//*[@id="crm-table"]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div').text)

    def test_kehu04_04(self):
        """验证快速创建客户功能是否正常"""
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(30)
        # 点击进入客户管理
        self.driver.find_element_by_xpath('//div[text()="客户管理"]').click()
        time.sleep(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“客户”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[2]/span').click()
        time.sleep(2)
        # 确定弹出框
        self.driver.switch_to.alert.accept()
        # 点击并输入客户名称
        self.driver.find_element_by_xpath('//form/div[1]/div/div[1]/input').click()
        self.driver.find_element_by_xpath('//form/div[1]/div/div[1]/input').send_keys("马老师")
        # 保存
        self.driver.find_element_by_xpath('//div[@class="handle-bar"]/button[3]').click()
        time.sleep(2)
        # 点击进入客户列表
        self.driver.find_element_by_xpath('//li/span[text()="客户"]').click()
        time.sleep(2)
        # 查看是否有该条客户信息
        text = self.driver.find_element_by_xpath('//*[@id="crm-table"]/div[4]/div[2]/table/tbody/tr[1]/td[3]/div').text
        print("text:"+text)
        self.assertEqual(text, "马老师")

    def test_kehu04_05(self):
        """验证快速创建联系人功能是否正常"""
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(30)
        # 点击进入客户管理
        self.driver.find_element_by_xpath('//div[text()="客户管理"]').click()
        time.sleep(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“联系人”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[3]/span').click()
        time.sleep(2)
        # 点击并输入联系人姓名
        self.driver.find_element_by_xpath('//form/div[1]/div/div[1]/input').click()
        self.driver.find_element_by_xpath('//form/div[1]/div/div[1]/input').send_keys("金轮")
        # 保存
        self.driver.find_element_by_xpath('//div[@class="handle-bar"]/button[2]').click()
        time.sleep(2)
        # 点击进入联系人列表
        self.driver.find_element_by_xpath('//li/span[text()="联系人"]').click()
        time.sleep(2)
        # 查看是否有该条联系人信息
        text = self.driver.find_element_by_xpath('//*[@id="crm-table"]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div').text
        print("text:"+text)
        self.assertEqual(text, "金轮")

    def test_kehu04_06(self):
        """验证将客户移入公海功能是否正常"""
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(30)
        # 点击进入客户管理
        self.driver.find_element_by_xpath('//div[text()="客户管理"]').click()
        time.sleep(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“客户”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[2]/span').click()
        time.sleep(2)
        # 确定弹出框
        self.driver.switch_to.alert.accept()
        # 点击并输入客户名称
        self.driver.find_element_by_xpath('//form/div[1]/div/div[1]/input').click()
        self.driver.find_element_by_xpath('//form/div[1]/div/div[1]/input').send_keys("芜湖")
        # 保存
        self.driver.find_element_by_xpath('//div[@class="handle-bar"]/button[3]').click()
        time.sleep(2)
        # 点击进入客户列表
        self.driver.find_element_by_xpath('//li/span[text()="客户"]').click()
        time.sleep(2)
        # 点击该条客户信息
        self.driver.find_element_by_xpath('//*[@id="crm-table"]/div[4]/div[2]/table/tbody/tr[1]/td[3]/div').click()
        # 勾选单选框，选择放入公海
        self.driver.find_element_by_xpath('//*[@id="crm-table"]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/span').click()
        self.driver.find_element_by_xpath('//div[text()="放入公海"]').click()
        # 点击确定
        self.driver.find_element_by_xpath('//div[@class="el-message-box__btns"]/button[2]').click()
        # 点击进入公海页面查看是否有该信息
        self.driver.find_element_by_xpath('//li/span[text()="公海"]').click()
        time.sleep(2)
        # 查看是否有该条客户信息
        text = self.driver.find_element_by_xpath('//*[@id="crm-table"]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div').text
        print("text:" + text)
        self.assertEqual(text, "芜湖")

    def test_kehu04_07(self):
        """验证快速创建产品功能是否正常"""
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(30)
        # 点击进入客户管理
        self.driver.find_element_by_xpath('//div[text()="客户管理"]').click()
        time.sleep(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“产品”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[7]/span').click()
        time.sleep(2)
        # 点击选择产品类型
        self.driver.find_element_by_xpath('//span[@class="el-cascader__label"]').click()
        self.driver.find_element_by_xpath('//li[@id="menu-7316-0-0"]').click()
        # 点击输入产品编码
        self.driver.find_element_by_xpath('//form/div[3]/div/div[1]/input').click()
        self.driver.find_element_by_xpath('//form/div[3]/div/div[1]/input').send_keys('abc1234')
        # 点击输入产品价格
        self.driver.find_element_by_xpath('//form/div[4]/div/div[1]/input').click()
        self.driver.find_element_by_xpath('//form/div[4]/div/div[1]/input').send_keys('100')
        # 点击选择产品上下架
        self.driver.find_element_by_xpath('//form/div[6]/div/div/div[1]/input').click()
        self.driver.find_element_by_xpath('//span[text()="上架"]').click()
        # 保存
        self.driver.find_element_by_xpath('//div[@class="handle-bar"]/button[2]').click()
        time.sleep(2)
        # 点击进入产品列表
        self.driver.find_element_by_xpath('//li/span[text()="产品"]').click()
        time.sleep(2)
        # 查看是否有该条产品信息
        text = self.driver.find_element_by_xpath('//*[@id="crm-table"]/div[3]/table/tbody/tr[1]/td[4]/div').text
        print("text:"+text)
        self.assertEqual(text, "abc1234")

    def test_kehu04_08(self):
        """验证仪表盘时间下拉框默认文本是否正常显示"""
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(30)
        # 点击进入客户管理
        self.driver.find_element_by_xpath('//div[text()="客户管理"]').click()
        time.sleep(15)
        # 获取下拉框的默认属性值
        timeFrame = self.driver.find_element_by_xpath('//input[@placeholder="请选择选择"]').get_attribute('value')
        print("timeFrame:" + timeFrame)
        # 比较
        self.assertEqual("本年", timeFrame)

    def test_houtai05_01(self):
        """验证修改企业名称后首页能否正常显示名称"""
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(15)
        # 点击右上角用户头像控件
        self.driver.find_element_by_xpath('//div[@class="user-container el-popover__reference"]').click()
        # 点击进入企业后台
        self.driver.find_element_by_xpath('//span[text()="进入企业管理后台"]').click()
        # 获取初始的企业名称
        name1 = self.driver.find_element_by_xpath('//div[@class="body"]/div[1]/div[2]/input').get_attribute("value")
        print(name1)
        # 点击企业名称输入框
        self.driver.find_element_by_xpath('//div[@class="body"]/div[1]/div[2]/input').click()
        self.driver.find_element_by_xpath('//div[@class="body"]/div[1]/div[2]/input').clear()
        self.driver.find_element_by_xpath('//div[@class="body"]/div[1]/div[2]/input').send_keys("bcbxCRM")
        # 保存
        self.driver.find_element_by_xpath('//span[text()="保存"]').click()
        # 退出系统
        self.driver.find_element_by_xpath('//div[text()="退出系统"]').click()
        # 确定
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]/span').click()
        # 获取登录页的名称进行对比
        name2 = self.driver.find_element_by_xpath('//div[@class="title"]').text
        print(name2)
        self.assertNotEqual(name2, name1)

if __name__ == "__main__":
    unittest.main()
