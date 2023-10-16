
import pytest
from selenium.webdriver.common.by import By
from pytest_cms.page.login import LoginPage
from pytest_cms.page.home import HomePage
from pytest_cms.page.base import CMSUtils

from pytest_cms.fixture.cms_web_fixture import *
import allure
import time


@pytest.fixture(scope='module')
def inHomePageMgr(get_cmsUtils):
    # 先登录
    return HomePage(utils=get_cmsUtils)


@allure.title("测试新增组件")
@allure.description("各种类型的组件，这个需要使用parameter 注解")
def test_component_add(inHomePageMgr: HomePage):
    print("测试新增组件")
    inHomePageMgr.add_component("name", "desc", "标签")
    assert 0 == 0

@allure.title("测试删除组件")
@allure.description("测试删除组件")
def test_component_del(inHomePageMgr: HomePage):
    print("测试删除组件")