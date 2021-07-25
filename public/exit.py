import time

class Myexit(object):
    # 初始化init方法接收driver避免启动两次窗口
    def __init__(self, driver):
        self.driver = driver

    # 退出系统
    def exitSys(self):
        self.driver.implicitly_wait(15)
        # 点击右上角用户头像控件
        self.driver.find_element_by_xpath('//div[@class="user-container el-popover__reference"]').click()
        # 点击退出登录按钮
        self.driver.find_element_by_xpath('//div[@class="handel-items"]/div[2]').click()
        time.sleep(2)
        # 点击“确定”按钮
        self.driver.find_element_by_xpath('//div[@class="el-message-box__btns"]/button[2]').click()
        time.sleep(3)
