class MyloginApp(object):
    # 初始化init方法接收driver避免启动两次窗口
    def __init__(self, driver):
        self.driver = driver

    # 封装app初始化设置
    def initialSetup(self):
        self.driver.implicitly_wait(15)
        # 首先进行一些列初始化的点击操作进入首页
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='同意']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/ivMaleLayout']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/ic_search_b']").click()

    # 封装登录方法
    def login(self):
        # 点击“我的”按钮
        self.driver.find_element_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/me_item']").click()
        # 进行登录操作
        self.driver.find_element_by_xpath("//*[@text='立即登录/注册']").click()
        self.driver.find_element_by_xpath("//*[@text='密码登录']").click()
        self.driver.find_element_by_xpath("//*[@text='请输入手机号']").click()
        self.driver.find_element_by_xpath("//*[@text='请输入手机号']").send_keys('15127409611')
        self.driver.find_element_by_xpath("//*[@text='请输入密码']").click()
        self.driver.find_element_by_xpath("//*[@text='请输入密码']").send_keys('a123456')
        self.driver.find_element_by_xpath("//*[@text='登  录']").click()
