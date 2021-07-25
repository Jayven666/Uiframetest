import os
import unittest
import time
from public.loginApp import MyloginApp
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )


class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        # 平台
        desired_caps['platformName'] = 'Android'
        # 系统版本
        desired_caps['platformVersion'] = '7.1'
        # 设备名称：不会强制校验，有变量名即可
        desired_caps['deviceName'] = 'Android Emulator'
        # 重装app，保证每一条数据都是从头开始的,noReset=False不一定会完全清除数据
        desired_caps['fullReset'] = 'True'
        # PATH("D:/软件测试/day24_5.23/zuiyou.apk")
        desired_caps['app'] = "D:/软件测试/day24_5.23/zuiyou.apk"
        # app的包名：唯一的。
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        # adb shell dumpsys activity top|findstr "ACTIVITY"
        desired_caps['appActivity'] = '.ui.base.SplashActivity'
        # 通过Uiautomator2对toast进行处理
        desired_caps['automationName'] = 'Uiautomator2'
        # 以Unicode形式输入中文
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        # 初始化driver，Remote远程链接发出请求，请求=请求的地址+路径
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        # 调用截图方法
        filedir = "D:/软件测试/day24_5.23/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', '软件测试', 'day24_5.23', 'screenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def testshouye01_01(self):
        """验证首页导航栏文案显示是否正常"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 点击“最右”首页按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        # 定位导航文本的列表
        navText = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        # 输出一下文本看看
        print(navText[0].text+"/"+navText[1].text+"/"+navText[2].text+"/"+navText[3].text)
        # 用assertEqual进行比较
        self.assertEqual(navText[0].text, "话题")
        self.assertEqual(navText[1].text, "推荐")
        self.assertEqual(navText[2].text, "视频")
        self.assertEqual(navText[3].text, "图文")

    def testshouye01_02(self):
        """验证刷新按钮是否正常"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 点击“最右”首页按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        # 获取当前第一篇帖子的发帖人
        name1 = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/simple_member_tv_name")
        firstName1 = name1[0].text
        print("第一篇帖子发帖人："+firstName1)
        # 获取当前第一篇帖子的标题
        title1 = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        firstTitle1 = title1[0].text
        print("第一篇帖子标题："+firstTitle1)
        # 点击刷新按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_refresh_view").click()
        # 获取当前第一篇帖子的发帖人
        name2 = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/simple_member_tv_name")
        firstName2 = name2[0].text
        print("刷新后的发帖人：" + firstName2)
        # 获取当前第一篇帖子的标题
        title2 = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        firstTitle2 = title2[0].text
        print("刷新后的标题：" + firstTitle2)
        # 用assertNotEqual进行比较
        self.assertNotEqual(firstName1, firstName2)
        self.assertNotEqual(firstTitle1, firstTitle2)

    def testshouye01_03(self):
        """验证搜索功能是否正常"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 点击“最右”首页按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        # 点击右上角“搜索按钮”进入搜索页面
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        # 点击搜索框，输入测试内容“test”
        search = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input")
        search.click()
        search.send_keys("test")
        time.sleep(2)
        # 获取第一条结果的话题名
        searchNames = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        searchName = searchNames[0].text
        print("搜索结果的话题名为：" + searchName)
        # 通过坐标定位第一条搜索结果，并点击进入
        self.driver.swipe(140, 230, 140, 230, 100)
        # 获取话题详情页的话题名称
        resName = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvTopicName").text
        print("话题详情的话题名为："+resName)
        # 用assertEqual对该话题的名称和搜索结果的名称进行比较，一样则说明跳转成功
        self.assertEqual(searchName, resName)

    def testshouye01_04(self):
        """验证无搜索结果的文案显示是否正常"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 点击“最右”首页按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        # 点击右上角“搜索按钮”进入搜索页面
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        # 点击搜索框，输入测试内容“？？？？？”
        search = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input")
        search.click()
        search.send_keys("？？？？？")
        time.sleep(2)
        # 获取无搜索结果时的文案
        noResText = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvTip").text
        print("无搜索结果的文案："+noResText)
        # 用assertEqual进行比较
        self.assertEqual(noResText, "打开方式不对，换个关键词试试~")

    def testshouye01_05(self):
        """验证能否正常打开帖子详情页"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 点击“最右”首页按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        # 获取第一篇帖子的标题信息并点击标题进入详情页
        titles = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        title1 = titles[0].text
        print("第一篇帖子的标题为："+title1)
        titles[0].click()
        # 获取详情页中的帖子标题
        title2 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvPostContent").text
        print("详情页的标题为：" + title2)
        # 用assertEqual进行比较
        self.assertEqual(title1, title2)

    def testshouye01_06(self):
        """验证评论帖子功能是否正常"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 点击“最右”首页按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        # 点击第一篇帖子的标题进入详情页
        titles = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        titles[0].click()
        # 定位评论框，点击后输入评论内容“test123”
        ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput")
        ele.click()
        ele.send_keys("test123")
        # 定位“发送”按钮点击发送
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
        # 定义一个元组，不管是什么路径只要text中包含评论发送成功就说明弹出了toast
        toast_loc = ("xpath", '//*[contains(@text,"评论发送成功")]')
        el = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
        print(el.text)

    def testshouye01_07(self):
        """验证首页下拉刷新是否正常"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 点击“最右”首页按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        # 获取当前第一篇帖子的发帖人
        name1 = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/simple_member_tv_name")
        firstName1 = name1[0].text
        print("第一篇帖子发帖人：" + firstName1)
        # 获取当前第一篇帖子的标题
        title1 = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        firstTitle1 = title1[0].text
        print("第一篇帖子标题：" + firstTitle1)
        # 从中心点(360,640)下拉至(360,840)进行刷新
        self.driver.swipe(360, 500, 360, 1000, 1000)
        time.sleep(5)
        # 获取当前第一篇帖子的发帖人
        name2 = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/simple_member_tv_name")
        firstName2 = name2[0].text
        print("刷新后的发帖人：" + firstName2)
        # 获取当前第一篇帖子的标题
        title2 = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        firstTitle2 = title2[0].text
        print("刷新后的标题：" + firstTitle2)
        # 用assertNotEqual进行比较
        self.assertNotEqual(firstName1, firstName2)
        self.assertNotEqual(firstTitle1, firstTitle2)

    def testshouye01_08(self):
        """验证首页屏蔽帖子功能是否正常"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 点击“最右”首页按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        # 获取当前第一篇帖子的标题
        title1 = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        firstTitle1 = title1[0].text
        print("第一篇帖子标题：" + firstTitle1)
        # 获取当前第一篇帖子的屏蔽按钮并点击
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/simple_decorator_delete").click()
        # 选择第一项理由进行屏蔽
        reasons = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/tvContent")
        reasons[0].click()
        # 获取当前第一篇帖子的标题
        title2 = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        firstTitle2 = title2[0].text
        print("屏蔽后的标题：" + firstTitle2)
        # 用assertNotEqual进行比较
        self.assertNotEqual(firstTitle1, firstTitle2)

    def testshouye01_09(self):
        """验证首页底部文案显示是否正常"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 点击“最右”首页按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        # 定位底部文本的列表
        bottomText = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/textTabItem")
        # 输出一下文本看看
        print(bottomText[0].text+"/"+bottomText[1].text+"/"+bottomText[2].text+"/"+bottomText[3].text)
        # 用assertEqual进行比较
        self.assertEqual(bottomText[0].text, "最右")
        self.assertEqual(bottomText[1].text, "发现")
        self.assertEqual(bottomText[2].text, "消息")
        self.assertEqual(bottomText[3].text, "我的")

if __name__ == "__main__":
    unittest.main()
