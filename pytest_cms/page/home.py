from selenium.webdriver.common.by import By
from pytest_cms.page.base import BasePage
from pytest_cms.config.cfg import *
import time


# 问题：
# 1. 如何切换测试环境
# 2. 有一个问题，碰到一闪而过的弹窗 如何暂停
# ##

class HomePage(BasePage):
    
    def __init__(self, utils):
        super().__init__(utils)

    def add_component(self, name, desc, tag):
        '''add component test'''
        self.open_url(CMSURL.COMPONENT.value)
        print("新增组件")
        time.sleep(2)