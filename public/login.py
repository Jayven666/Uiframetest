import time


class Mylogin(object):
    # 初始化init方法接收driver避免启动两次窗口
    def __init__(self, driver):
        self.driver = driver

    # 老密码登录
    def oldLogin(self):
        # 输入用户名
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').send_keys(
            "13676083391")
        # 输入密码
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/input').send_keys("123djw")
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[4]/div/button').click()
        time.sleep(5)

    # 新密码登录，因为有修改密码的用例
    def newLogin(self):
        # 输入用户名
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').send_keys(
            "13676083391")
        # 输入密码
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/input').send_keys("123456")
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[4]/div/button').click()
        time.sleep(5)

    # 审批人账号登录
    def adminLogin(self):
        # 输入用户名
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').send_keys(
            "admin")
        # 输入密码
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/input').send_keys("123456")
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[4]/div/button').click()
        time.sleep(5)
