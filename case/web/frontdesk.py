# coding=utf-8
from selenium import webdriver
from public.login import Mylogin
from selenium.webdriver.common.keys import Keys
import unittest
import os
import time


class TestBackStage(unittest.TestCase):
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

    # test方法，一个test方法对应一条手工测试用例，要以test开头+测试用例的编号
    def test_qiantai01_01(self):
        """验证登录账号的手机号是否一致"""
        # 1.登录，调用公共包里登录模块的登陆方法
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(15)
        # 2.点击右上角用户头像控件
        self.driver.find_element_by_xpath('//div[@class="user-container el-popover__reference"]').click()
        # 3.点击个人中心，跳转个人信息页面
        self.driver.find_element_by_xpath('//div[@class="handel-items"]/div[1]').click()
        # 4.定位手机号（登录名）信息
        phoneNum = self.driver.find_element_by_xpath('//div[@class="section"]/div[2]/div[3]/div/div[2]').text
        print("phoneNum:" + phoneNum)
        # 5.比较
        self.assertEqual("13676083391", phoneNum)

    def test_qiantai01_02(self):
        """验证编辑功能是否正常"""
        # 因为要编辑会有全选删除操作所以需要使用Keys类，导入一下
        # 1.登录，调用公共包里登录模块的登陆方法
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(15)
        # 2.点击右上角用户头像控件
        self.driver.find_element_by_xpath('//div[@class="user-container el-popover__reference"]').click()
        # 3.点击个人中心，跳转个人信息页面
        self.driver.find_element_by_xpath('//div[@class="handel-items"]/div[1]').click()
        # 4.点击“编辑”按钮弹出编辑页面
        self.driver.find_element_by_xpath('//div[@class="header-handle"]/button[2]').click()
        # 5.定位姓名和邮箱输入框进行修改后保存，这里尝试用css_selector定位，xpath写的太多了
        # 名字默认修改为testName，邮箱默认修改为testMail@bcbx.com
        # 对于输入框想修改应该:点击→全选→删除→输入
        name = self.driver.find_element_by_css_selector("div.person-container>div:nth-child(7)>div>div:nth-child(2)>form>div:first-child>div>div>input")
        name.click()
        name.send_keys(Keys.CONTROL, "a")
        name.send_keys(Keys.BACK_SPACE)
        name.send_keys("testName")
        mail = self.driver.find_element_by_css_selector("div.person-container>div:nth-child(7)>div>div:nth-child(2)>form>div:nth-child(2)>div>div>input")
        mail.click()
        mail.send_keys(Keys.CONTROL, "a")
        mail.send_keys(Keys.BACK_SPACE)
        mail.send_keys("testMail@bcbx.com")
        time.sleep(2)
        # 6.点击保存按钮，因为保存操作需要一定时间所以要加强制等待时间
        self.driver.find_element_by_xpath('//div[@class="person-container"]/div[6]/div/div[3]/span/button[1]').click()
        time.sleep(2)
        # 7.定位姓名和邮箱信息
        nameBox = self.driver.find_element_by_xpath('//div[@class="section"]/div[2]/div[1]/div/div[2]').text
        mailBox = self.driver.find_element_by_xpath('//div[@class="section"]/div[2]/div[4]/div/div[2]').text
        print("nameBox:" + nameBox)
        print("mailBox:" + mailBox)
        # 8.比较
        self.assertEqual("testName", nameBox)
        self.assertEqual("testMail@bcbx.com", mailBox)

    def test_qiantai01_03(self):
        """验证“修改密码”功能是否正常"""
        # 1.登录，调用公共包里登录模块的登陆方法
        Mylogin(self.driver).oldLogin()
        self.driver.implicitly_wait(15)
        # 2.点击右上角用户头像控件
        self.driver.find_element_by_xpath('//div[@class="user-container el-popover__reference"]').click()
        # 3.点击个人中心，跳转个人信息页面
        self.driver.find_element_by_xpath('//div[@class="handel-items"]/div[1]').click()
        # 4.点击“修改密码”按钮弹出编辑页面
        self.driver.find_element_by_xpath('//div[@class="header-handle"]/button[1]').click()
        # 5.定位原密码输入框点击进行修改后保存
        oldPwd = self.driver.find_element_by_xpath('//form[@class="el-form el-form--label-top"]/div[1]/div/div/input')
        oldPwd.click()
        oldPwd.send_keys("123djw")
        # 定位新密码输入框点击进行修改后保存
        newPwd = self.driver.find_element_by_xpath('//form[@class="el-form el-form--label-top"]/div[2]/div/div/input')
        newPwd.click()
        newPwd.send_keys("123456")
        time.sleep(2)
        # 6.点击保存按钮，因为保存操作需要一定时间所以要加强制等待时间
        self.driver.find_element_by_xpath('//div[@class="person-container"]/div[7]/div/div[3]/span/button[1]').click()
        time.sleep(2)
        # 7.点击确定
        self.driver.find_element_by_xpath('//div[@class="el-message-box__btns"]/button').click()
        # 8.调用新的登录
        Mylogin(self.driver).newLogin()
        # 9.判断是否已经登录成功
        # 通过判断工作台的导航文本从左往右“全部、日志、审批、任务、日程、公告”
        self.assertEqual(self.driver.find_element_by_id("tab-0").text, "全部")
        self.assertEqual(self.driver.find_element_by_id("tab-1").text, "日志")
        self.assertEqual(self.driver.find_element_by_id("tab-5").text, "审批")
        self.assertEqual(self.driver.find_element_by_id("tab-4").text, "任务")
        self.assertEqual(self.driver.find_element_by_id("tab-2").text, "日程")
        self.assertEqual(self.driver.find_element_by_id("tab-3").text, "公告")
        # 通过工作台控件是否已经加载出来进行判断
        self.assertTrue(self.driver.find_element_by_xpath("//li[@class='el-menu-item menu-item-defalt is-active menu-item-select']").is_displayed())

    def test_qiantai01_04(self):
        """验证返回功能是否正常"""
        # 1.登录，调用公共包里登录模块的登陆方法
        Mylogin(self.driver).newLogin()
        self.driver.implicitly_wait(15)
        # 2.点击右上角用户头像控件
        self.driver.find_element_by_xpath('//div[@class="user-container el-popover__reference"]').click()
        # 3.点击个人中心，跳转个人信息页面
        self.driver.find_element_by_xpath('//div[@class="handel-items"]/div[1]').click()
        # 4.点击“返回”按钮
        self.driver.find_element_by_xpath('//button[@class="el-button el-button--default is-plain"]').click()
        # 5.判断是否已经登录成功
        # 通过判断工作台的导航文本从左往右“全部、日志、审批、任务、日程、公告”
        self.assertEqual(self.driver.find_element_by_id("tab-0").text, "全部")
        self.assertEqual(self.driver.find_element_by_id("tab-1").text, "日志")
        self.assertEqual(self.driver.find_element_by_id("tab-5").text, "审批")
        self.assertEqual(self.driver.find_element_by_id("tab-4").text, "任务")
        self.assertEqual(self.driver.find_element_by_id("tab-2").text, "日程")
        self.assertEqual(self.driver.find_element_by_id("tab-3").text, "公告")
        # 通过导航栏控件是否已经加载出来进行判断
        self.assertTrue(self.driver.find_element_by_xpath(
            "//a[@class='nav-item router-link-active']").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath(
            "//i[@class='wukong wukong-customer']").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath(
            "//i[@class='wukong wukong-statistics']").is_displayed())

    def test_qiantai01_05(self):
        """验证退出登录功能是否正常"""
        # 1.登录，调用公共包里登录模块的登陆方法
        Mylogin(self.driver).newLogin()
        self.driver.implicitly_wait(15)
        # 2.点击右上角用户头像控件
        self.driver.find_element_by_xpath('//div[@class="user-container el-popover__reference"]').click()
        # 3.点击退出登录按钮
        self.driver.find_element_by_xpath('//div[@class="handel-items"]/div[2]').click()
        time.sleep(2)
        # 4.点击“确定”按钮
        self.driver.find_element_by_xpath('//div[@class="el-message-box__btns"]/button[2]').click()
        time.sleep(3)
        # 5.验证是否为登录页面
        username = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input')
        self.assertTrue(username.is_displayed())
        self.assertEqual(username.get_attribute("placeholder"), "请输入用户名")
        password = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/input')
        self.assertTrue(password.is_displayed())
        self.assertEqual(password.get_attribute("placeholder"), "请输入密码")

if __name__ == "__main__":
    unittest.main()
