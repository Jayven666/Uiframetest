# coding=utf-8
from selenium import webdriver
import unittest
import os
import time
from public.login import Mylogin
from public.exit import Myexit
from selenium.webdriver.common.keys import Keys

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

    def test_bangong02_01(self):
        """验证快速创建日志功能是否正常"""
        Mylogin(self.driver).newLogin()
        self.driver.implicitly_wait(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“日志”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[1]/span').click()
        time.sleep(2)
        # 点击“今日工作”内容框
        todayWork = self.driver.find_element_by_xpath('//div[@class="form"]/div[1]/div/textarea')
        todayWork.click()
        todayWork.send_keys("web自动化用例")
        # 点击“明日工作”内容框
        todayWork = self.driver.find_element_by_xpath('//div[@class="form"]/div[2]/div/textarea')
        todayWork.click()
        todayWork.send_keys("CI/CD")
        # 点击“遇到的问题”内容框
        todayWork = self.driver.find_element_by_xpath('//div[@class="form"]/div[3]/div/textarea')
        todayWork.click()
        todayWork.send_keys("暂无")
        # 点击“提交”按钮
        self.driver.find_element_by_xpath('//div[@class="btn-group"]/button[1]').click()
        time.sleep(3)
        # 判断是否有该日志
        today = self.driver.find_element_by_xpath('//div[@id="journal-cell0"]/div[1]/div[2]/p[1]').text
        self.assertIn("web自动化用例", today )
        tomorrow = self.driver.find_element_by_xpath('//div[@id="journal-cell0"]/div[1]/div[2]/p[2]').text
        self.assertIn("CI/CD", tomorrow)
        problem = self.driver.find_element_by_xpath('//div[@id="journal-cell0"]/div[1]/div[2]/p[3]').text
        self.assertIn("暂无", problem)
        # 通过导航栏控件是否已经加载出来进行判断
        self.assertTrue(self.driver.find_element_by_xpath(
            "//a[@class='nav-item router-link-active']").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath(
            "//i[@class='wukong wukong-customer']").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath(
            "//i[@class='wukong wukong-statistics']").is_displayed())

    def test_bangong02_02(self):
        """验证快速创建任务功能是否正常"""
        Mylogin(self.driver).newLogin()
        self.driver.implicitly_wait(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“日志”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[3]/span').click()
        time.sleep(2)
        # 点击“任务名称”输入框输入内容
        task = self.driver.find_element_by_xpath('//div[@class="el-input"]/input')
        task.click()
        task.send_keys("完成课后作业")
        # 选择admin为负责人
        principal = self.driver.find_element_by_xpath('//div[@class="select-box el-popover__reference"]')
        principal.click()
        # 搜索admin
        search = self.driver.find_element_by_xpath('//input[@placeholder="搜索成员"]')
        search.click()
        search.send_keys("admin")
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[@class="el-checkbox__label"]').click()
        # 选择“任务描述”框输入
        self.driver.find_element_by_xpath('//textarea[@class="el-textarea__inner"]').click()
        self.driver.find_element_by_xpath('//textarea[@class="el-textarea__inner"]').send_keys("测试test")
        # 保存
        self.driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]').click()
        time.sleep(3)
        # 查看页面中任务标题是否加载出来
        self.assertTrue(self.driver.find_element_by_xpath('//div[@id="pane-mytask"]/div/div[3]/div/div/div[1]/span').is_displayed())
        self.assertEqual(self.driver.find_element_by_xpath('//div[@id="pane-mytask"]/div/div[3]/div/div/div[1]/span').text, "完成课后作业")

    def test_bangong02_03(self):
        """验证任务详情页完成任务功能是否正常"""
        Mylogin(self.driver).newLogin()
        self.driver.implicitly_wait(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“日志”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[3]/span').click()
        time.sleep(2)
        # 点击“任务名称”输入框输入内容
        task = self.driver.find_element_by_xpath('//div[@class="el-input"]/input')
        task.click()
        task.send_keys("任务测试")
        # 选择admin为负责人
        principal = self.driver.find_element_by_xpath('//div[@class="select-box el-popover__reference"]')
        principal.click()
        # 搜索admin
        search = self.driver.find_element_by_xpath('//input[@placeholder="搜索成员"]')
        search.click()
        search.send_keys("admin")
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[@class="el-checkbox__label"]').click()
        # 选择“任务描述”框输入
        self.driver.find_element_by_xpath('//textarea[@class="el-textarea__inner"]').click()
        self.driver.find_element_by_xpath('//textarea[@class="el-textarea__inner"]').send_keys("测试test")
        # 保存
        self.driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]').click()
        time.sleep(3)
        # 点击任务进入详情页
        self.driver.find_element_by_xpath('//div[@id="pane-mytask"]/div/div[3]/div/div/div[1]/span').click()
        choose = self.driver.find_element_by_xpath('//div[@id="pane-mytask"]/div/div[4]/div[2]/div[1]/div[1]/label/span/span')
        self.driver.execute_script("arguments[0].click();", choose)
        # 刷新页面
        self.driver.refresh()
        time.sleep(5)
        # 验证刷新后找不到该控件
        self.assertEqual(self.driver.find_element_by_xpath('//div[@id="pane-mytask"]/div/div[3]/p/button/span').text, "没有更多了")

    def test_bangong02_04(self):
        """验证任务标签下搜索功能是否能够进行模糊匹配"""
        Mylogin(self.driver).newLogin()
        self.driver.implicitly_wait(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“日志”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[3]/span').click()
        time.sleep(2)
        # 点击“任务名称”输入框输入内容
        task = self.driver.find_element_by_xpath('//div[@class="el-input"]/input')
        task.click()
        task.send_keys("test任务测试")
        # 选择admin为负责人
        principal = self.driver.find_element_by_xpath('//div[@class="select-box el-popover__reference"]')
        principal.click()
        # 搜索admin
        search = self.driver.find_element_by_xpath('//input[@placeholder="搜索成员"]')
        search.click()
        search.send_keys("admin")
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[@class="el-checkbox__label"]').click()
        # 保存
        self.driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]').click()
        time.sleep(3)
        # 点击搜索框，只输入t搜索，进行模糊匹配
        self.driver.find_element_by_xpath('//div[@id="pane-mytask"]/div/div[1]/div/input').click()
        self.driver.find_element_by_xpath('//div[@id="pane-mytask"]/div/div[1]/div/input').send_keys("t")
        # 判断搜索结果是否有和任务标题一样
        self.assertTrue(self.driver.find_element_by_xpath('//div[@id="pane-mytask"]/div/div[3]/div/div/div[1]/span').is_displayed())
        self.assertEqual(self.driver.find_element_by_xpath('//div[@id="pane-mytask"]/div/div[3]/div/div/div[1]/span').text, "test任务测试")

    def test_bangong02_05(self):
        """验证快速创建审批功能是否正常"""
        Mylogin(self.driver).newLogin()
        self.driver.implicitly_wait(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“日志”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[2]/span').click()
        time.sleep(2)
        # 点击“普通审批”按钮
        self.driver.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[1]').click()
        # 填写审批信息（内容，备注，审核人）
        # 审批内容
        aptContent = self.driver.find_element_by_xpath('//div[@class="el-form-item__content"]/div/input')
        aptContent.click()
        aptContent.send_keys("Test审批功能")
        # 备注
        remarks = self.driver.find_element_by_xpath('//div[@class="el-form-item__content"]/div/textarea')
        remarks.click()
        remarks.send_keys("验证快速创建审批功能是否正常")
        # 定位添加审核人
        self.driver.find_element_by_css_selector('div.add-item').click()
        # 搜索admin并选择
        search = self.driver.find_element_by_xpath('//input[@placeholder="搜索成员"]')
        search.click()
        search.send_keys("admin")
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[@class="el-checkbox__label"]').click()
        # 保存
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[3]/button[2]').click()
        time.sleep(3)
        # 点击审批标签查看
        self.driver.find_element_by_xpath('//div[@id="app"]/section/section/aside/div/ul/a[6]/li').click()
        time.sleep(2)
        # 先定位该标签内容是否显示出来
        self.assertTrue(self.driver.find_element_by_xpath('//div[@id="examine-list-boxmy"]/div[1]/div/div[2]/p').is_displayed())
        # 再通过父级定位其状态是否为待审
        status = self.driver.find_element_by_xpath('//div[@id="examine-list-boxmy"]/div[1]/div/div[2]/p/../../div[1]/div[3]/span[2]/span[2]')
        self.assertEqual(status.text, "待审")

    def test_bangong02_06(self):
        """验证通过审批功能是否正常"""
        Mylogin(self.driver).newLogin()
        self.driver.implicitly_wait(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“审批”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[2]/span').click()
        time.sleep(2)
        # 点击“普通审批”按钮
        self.driver.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[1]').click()
        # 填写审批信息（内容，备注，审核人）
        # 审批内容
        aptContent = self.driver.find_element_by_xpath('//div[@class="el-form-item__content"]/div/input')
        aptContent.click()
        aptContent.send_keys("Test审批通过")
        # 备注
        remarks = self.driver.find_element_by_xpath('//div[@class="el-form-item__content"]/div/textarea')
        remarks.click()
        remarks.send_keys("验证通过审批功能是否正常")
        # 定位添加审核人
        self.driver.find_element_by_css_selector('div.add-item').click()
        # 搜索admin并选择
        search = self.driver.find_element_by_xpath('//input[@placeholder="搜索成员"]')
        search.click()
        search.send_keys("admin")
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[@class="el-checkbox__label"]').click()
        # 保存
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[3]/button[2]/span').click()
        time.sleep(3)
        # 调用退出方法，登录审批人的账号
        Myexit(self.driver).exitSys()
        Mylogin(self.driver).adminLogin()
        # 点击审批按钮-我的审批进入审批详情页
        self.driver.find_element_by_xpath('//div[@id="app"]/section/section/aside/div/ul/a[6]/li').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//div[@class="el-tabs__item is-top"]/div/span').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//p[text()="Test审批通过"]').click()
        time.sleep(2)
        # 点击通过，输入意见，确定
        self.driver.find_element_by_xpath('//button[@class="el-button flow-button blue el-button--default"]/span').click()
        self.driver.find_element_by_xpath('//textarea[@placeholder="请输入审批意见（选填）"]').click()
        self.driver.find_element_by_xpath('//textarea[@placeholder="请输入审批意见（选填）"]').send_keys("同意审批")
        self.driver.find_element_by_xpath('//div[@aria-label="审批通过"]/div[3]/div/button[2]').click()
        # 退出登录，登录申请人账号查看
        # 调用退出方法，登录审批人的账号
        Myexit(self.driver).exitSys()
        Mylogin(self.driver).newLogin()
        # 点击审批
        self.driver.find_element_by_xpath('//div[@id="app"]/section/section/aside/div/ul/a[6]/li').click()
        time.sleep(2)
        # 判断该审批的状态是否变为审核通过
        self.assertTrue(self.driver.find_element_by_xpath('//div[@id="examine-list-boxmy"]/div[1]/div/div[2]/p').is_displayed())
        # 再通过父级定位其状态是否为待审
        status = self.driver.find_element_by_xpath(
            '//div[@id="examine-list-boxmy"]/div[1]/div/div[2]/p/../../div[1]/div[3]/span[2]/span[2]')
        self.assertEqual(status.text, "审核通过")

    def test_bangong02_07(self):
        """验证通过审批功能是否正常"""
        Mylogin(self.driver).newLogin()
        self.driver.implicitly_wait(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“审批”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[2]/span').click()
        time.sleep(2)
        # 点击“普通审批”按钮
        self.driver.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[1]').click()
        # 填写审批信息（内容，备注，审核人）
        # 审批内容
        aptContent = self.driver.find_element_by_xpath('//div[@class="el-form-item__content"]/div/input')
        aptContent.click()
        aptContent.send_keys("Test审核拒绝")
        # 备注
        remarks = self.driver.find_element_by_xpath('//div[@class="el-form-item__content"]/div/textarea')
        remarks.click()
        remarks.send_keys("验证拒绝审批功能是否正常")
        # 定位添加审核人
        self.driver.find_element_by_css_selector('div.add-item').click()
        # 搜索admin并选择
        search = self.driver.find_element_by_xpath('//input[@placeholder="搜索成员"]')
        search.click()
        search.send_keys("admin")
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[@class="el-checkbox__label"]').click()
        # 保存
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[3]/button[2]/span').click()
        time.sleep(3)
        # 调用退出方法，登录审批人的账号
        Myexit(self.driver).exitSys()
        Mylogin(self.driver).adminLogin()
        # 点击审批按钮-我的审批进入审批详情页
        self.driver.find_element_by_xpath('//div[@id="app"]/section/section/aside/div/ul/a[6]/li').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//div[@class="el-tabs__item is-top"]/div/span').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//p[text()="Test审核拒绝"]').click()
        time.sleep(2)
        # 点击拒绝，输入意见，确定
        self.driver.find_element_by_xpath('//button[@class="el-button flow-button red el-button--default"]/span').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//textarea[@class="el-textarea__inner"]').click()
        self.driver.find_element_by_xpath('//textarea[@class="el-textarea__inner"]').send_keys("拒绝审批")
        self.driver.find_element_by_xpath('//div[@aria-label="审批拒绝"]/div[3]/div/button[2]').click()
        time.sleep(2)
        # 退出登录，登录申请人账号查看
        # 调用退出方法，登录审批人的账号
        Myexit(self.driver).exitSys()
        Mylogin(self.driver).newLogin()
        # 点击审批
        self.driver.find_element_by_xpath('//div[@id="app"]/section/section/aside/div/ul/a[6]/li').click()
        time.sleep(2)
        # 判断该审批的状态是否变为审核通过
        self.assertTrue(self.driver.find_element_by_xpath('//div[@id="examine-list-boxmy"]/div[1]/div/div[2]/p').is_displayed())
        # 再通过父级定位其状态是否为待审
        status = self.driver.find_element_by_xpath(
            '//div[@id="examine-list-boxmy"]/div[1]/div/div[2]/p/../../div[1]/div[3]/span[2]/span[2]')
        self.assertEqual(status.text, "审核拒绝")

    def test_bangong02_08(self):
        """验证撤回审批功能是否正常"""
        Mylogin(self.driver).newLogin()
        self.driver.implicitly_wait(15)
        # 点击“快速创建”按钮
        self.driver.find_element_by_xpath('//div[@class="create-button el-popover__reference"]').click()
        # 点击“审批”选项
        self.driver.find_element_by_xpath('//div[@class="quick-add"]/div/p[2]/span').click()
        time.sleep(2)
        # 点击“普通审批”按钮
        self.driver.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[1]').click()
        # 填写审批信息（内容，备注，审核人）
        # 审批内容
        aptContent = self.driver.find_element_by_xpath('//div[@class="el-form-item__content"]/div/input')
        aptContent.click()
        aptContent.send_keys("test审批撤回")
        # 备注
        remarks = self.driver.find_element_by_xpath('//div[@class="el-form-item__content"]/div/textarea')
        remarks.click()
        remarks.send_keys("验证撤回审批功能是否正常")
        # 定位添加审核人
        self.driver.find_element_by_css_selector('div.add-item').click()
        # 搜索admin并选择
        search = self.driver.find_element_by_xpath('//input[@placeholder="搜索成员"]')
        search.click()
        search.send_keys("admin")
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[@class="el-checkbox__label"]').click()
        # 保存
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[3]/button[2]/span').click()
        time.sleep(3)
        # 点击审批
        self.driver.find_element_by_xpath('//div[@id="app"]/section/section/aside/div/ul/a[6]/li').click()
        time.sleep(2)
        # 撤回审批
        self.driver.find_element_by_xpath('//div[@id="examine-list-boxmy"]/div[1]/div/div[1]/div[3]/div').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/ul/li[1]').click()
        # 定位撤回理由，确定
        self.driver.find_element_by_xpath('//textarea[@class="el-textarea__inner"]').click()
        self.driver.find_element_by_xpath('//textarea[@class="el-textarea__inner"]').send_keys("撤回审批")
        self.driver.find_element_by_xpath('//div[@aria-label="撤回审批"]/div[3]/div/button[2]').click()
        time.sleep(2)
        # 判断该审批的状态是否变为审核通过
        self.assertTrue(
            self.driver.find_element_by_xpath('//div[@id="examine-list-boxmy"]/div[1]/div/div[2]/p').is_displayed())
        # 再通过父级定位其状态是否为待审
        status = self.driver.find_element_by_xpath(
            '//div[@id="examine-list-boxmy"]/div[1]/div/div[2]/p/../../div[1]/div[3]/span[2]/span[2]')
        self.assertEqual(status.text, "撤回")

    def test_bangong02_09(self):
        """验证用户修改名字后通讯录姓名能否正常显示"""
        # 因为要编辑会有全选删除操作所以需要使用Keys类，导入一下
        Mylogin(self.driver).newLogin()
        self.driver.implicitly_wait(15)
        # 点击通讯录获取手机号对应的姓名
        self.driver.find_element_by_xpath('//div[@id="app"]/section/section/aside/div/ul/a[7]/li').click()
        time.sleep(2)
        name1 = self.driver.find_element_by_xpath('//span[text()="13676083391"]/../../../div[1]').text
        # 点击右上角用户头像控件
        self.driver.find_element_by_xpath('//div[@class="user-container el-popover__reference"]').click()
        # 点击个人中心，跳转个人信息页面
        self.driver.find_element_by_xpath('//div[@class="handel-items"]/div[1]').click()
        # 点击“编辑”按钮弹出编辑页面
        self.driver.find_element_by_xpath('//div[@class="header-handle"]/button[2]').click()
        # 名字默认修改为testName对于输入框想修改应该:点击→全选→删除→输入
        name = self.driver.find_element_by_css_selector(
            "div.person-container>div:nth-child(7)>div>div:nth-child(2)>form>div:first-child>div>div>input")
        name.click()
        name.send_keys(Keys.CONTROL, "a")
        name.send_keys(Keys.BACK_SPACE)
        name.send_keys("testjayven")
        # 点击保存按钮，因为保存操作需要一定时间所以要加强制等待时间
        self.driver.find_element_by_xpath('//div[@class="person-container"]/div[6]/div/div[3]/span/button[1]').click()
        time.sleep(2)
        # 点击返回
        self.driver.find_element_by_xpath('//button[@class="el-button el-button--default is-plain"]').click()
        # 再次通过手机号获取姓名，进行比较
        name2 = self.driver.find_element_by_xpath('//span[text()="13676083391"]/../../../div[1]').text
        self.assertNotEqual(name1, name2)

if __name__ == "__main__":
    unittest.main()
