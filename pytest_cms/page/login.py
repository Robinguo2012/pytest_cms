from selenium.webdriver.common.by import By
from pytest_cms.page.base import BasePage
from pytest_cms.config.cfg import *
import time


# 问题：
# 1. 如何切换测试环境
# 2. 有一个问题，碰到一闪而过的弹窗 如何暂停
# ##

class LoginPage(BasePage):
    
    def __init__(self, utils):
        super().__init__(utils)

    def login(self, username, password, authcode):
        '''login test'''
        self.open_url(CMSURL.LOGIN.value)
        time.sleep(3)

           # //input[@class='el-input__inner'][@placeholder='账号']
        if username is not None:
            ele = self.wd.find_element(by=By.XPATH, value="//input[@class='el-input__inner'][@placeholder='账号']")
            ele.clear()
            ele.send_keys(username)
        
        if password is not None:
            ele = self.wd.find_element(by=By.XPATH, value="//input[@class='el-input__inner'][@placeholder='密码']")
            ele.clear()
            ele.send_keys(password)
            
        
        if authcode is not None:
            self.wd.find_element(by=By.XPATH, value="//input[@class='el-input__inner'][@placeholder='验证码']").send_keys(authcode)

        # 点击登录
        loginBtn = self.wd.find_element(by=By.XPATH, value="//button[@class='el-button el-button--primary el-button--large']").click()
        
        time.sleep(2)