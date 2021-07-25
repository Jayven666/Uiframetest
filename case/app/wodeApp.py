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
        # 以Unicode形式输入中文
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        # 初始化driver，Remote远程链接发出请求，请求=请求的地址+路径
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        filedir = "D:/软件测试/day24_5.23/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', '软件测试', 'day24_5.23', 'screenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def testme02_01(self):
        """验证编辑签名功能是否正常"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 定位签名栏获取此时的签名信息并点击
        sign = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_member_sign").text
        print("原签名"+sign)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_member_sign").click()
        # 此时有首次弹窗，点击一下弹出的控件
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_zone").click()
        # 进入修改签名页面
        self.driver.find_element_by_xpath("//*[@text='编辑资料']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/tvSignOrLoginTips']").click()
        # 通过app中键盘事件修改签名
        # 这里写了个循环，获取文本长度后进行多次删除
        for i in range(0, len(sign)):
            self.driver.keyevent(67)
        # 循环结束，输入要修改的签名
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").send_keys("签名测试")
        # 保存
        self.driver.find_element_by_xpath('//*[@text="保存"]').click()
        # 再获取签名
        newSign = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvSignOrLoginTips").text
        print("新签名："+newSign)
        # 进行比较
        self.assertNotEqual(sign, newSign)

    def testme02_02(self):
        """验证点击最右ID复制功能是否正常"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 定位签名栏获取此时的签名信息并点击
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_member_sign").click()
        # 此时有首次弹窗，点击一下弹出的控件
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_zone").click()
        # 进入个人信息页面
        self.driver.find_element_by_xpath("//*[@text='编辑资料']").click()
        # 点击最右id
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/user_id").click()
        # 使用toast定位弹出的黑框
        toast_loc = ("xpath", '//*[contains(@text,"复制成功")]')
        el = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
        print(el.text)

    def testme02_03(self):
        """验证我的评论列表是否正常显示历史记录"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 先发布一条评论
        # 点击“最右”首页按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        # 点击第一篇帖子的标题进入详情页
        titles = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        # 获取帖子的话题文本
        topics = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/topic_tv")
        topic = topics[0].text
        titles[0].click()
        # 定位评论框，点击后输入评论内容“test123”
        ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput")
        ele.click()
        ele.send_keys("评论历史记录验证")
        # 定位“发送”按钮点击发送
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
        # 定义一个元组，不管是什么路径只要text中包含评论发送成功就说明弹出了toast
        toast_loc = ("xpath", '//*[contains(@text,"评论发送成功")]')
        el = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
        print(el.text)
        # 回到我的评论模块查看记录
        # 返回上一页面KEYCODE_BACK 返回键 4
        self.driver.keyevent(4)
        # 定位“我的”并点击
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()
        # 定位“我的评论”并点击
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/my_comment").click()
        # 弹出首次提示框，点击一下
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btnHide").click()
        # 查找评论内容，判断是否已经加载
        self.assertTrue(self.driver.find_element_by_xpath("//*[@text='评论历史记录验证']").is_displayed())
        # 再根据多个其他的控件一起进行判断
        self.assertEqual(self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvTitle").text, "我的评论")
        # 获取历史记录里的帖子话题
        tops = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/tvTopicName")
        top = tops[0].text
        self.assertIn(top, topic)

    def testme02_04(self):
        """验证我的发帖列表是否正常显示历史记录"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 点击“+”按钮
        self.driver.find_element_by_xpath('//android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout').click()
        # 选择第一个话题并添加
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/select_topic_enter").click()
        topics = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/topic_title_tv")
        # 获取话题文本
        topic = topics[0].text
        topics[0].click()
        time.sleep(2)
        # 输入要发布的内容
        self.driver.find_element_by_class_name("android.widget.EditText").click()
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys("最右app自动化测试")
        # 点击发布按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/try_publish").click()
        # 回到我的帖子模块查看记录
        # 定位“我的帖子”并点击
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/my_post").click()
        time.sleep(2)
        # 查找帖子内容，判断是否已经加载
        self.assertTrue(self.driver.find_element_by_xpath("//*[@text='最右app自动化测试']").is_displayed())
        # 再根据多个其他的控件一起进行判断
        self.assertEqual(self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title").text, "我的帖子")
        titles = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/topic_tv")
        title = titles[0].text
        self.assertIn(topic, title)

    def testme02_05(self):
        """验证退出当前帐号功能是否正常"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 定位设置按钮并点击
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/setting").click()
        # 定位退出账号选项并点击
        self.driver.find_element_by_xpath('//*[@text="退出当前账号"]').click()
        # 点击确定选项
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        # 登录/注册控件如果加载了出来就说明成功退出
        self.assertTrue(self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_notLogin_goLogin").is_displayed())
        # 再通过点击我的帖子按钮进行判断，如果弹出黑框要求登录，则说明退出成功
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/my_post").click()
        toast_loc = ("xpath", '//*[contains(@text,"请先登录")]')
        el = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
        print(el.text)

    def testme02_06(self):
        """验证清除缓存功能是否正常"""
        self.driver.implicitly_wait(15)
        # 调用初始化设置的方法
        MyloginApp(self.driver).initialSetup()
        # 调用登录方法
        MyloginApp(self.driver).login()
        # 定位设置按钮并点击
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/setting").click()
        # 定位清除缓存选项并点击
        self.driver.find_element_by_xpath('//*[@text="清除缓存"]').click()
        # 使用toast定位弹出的黑框
        toast_loc = ("xpath", '//*[contains(@text,"清除成功")]')
        el = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
        print(el.text)


if __name__ == "__main__":
    unittest.main()
