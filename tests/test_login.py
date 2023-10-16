
import pytest
from selenium.webdriver.common.by import By
from pytest_cms.page.login import LoginPage
from pytest_cms.page.base import CMSUtils
from pytest_cms.fixture.cms_web_fixture import *
import allure
import time



@pytest.fixture(scope='module')
def inLoginModule(get_cmsUtils):
    return LoginPage(utils=get_cmsUtils)
    

@pytest.fixture(scope='module', autouse=True)
def browser_quit(get_cmsUtils):

    yield
    time.sleep(3)
    get_cmsUtils.wd.quit()


@allure.title("测试成功")
@allure.description("登录成功的场景测试")
@pytest.mark.parametrize('username, password, authcode, exceptedText',[
    # ('admin123', '123456', '123456', '账户名或密码错误'),
    ('admin', '123456', '123456', '系统接口请求超时')
])
def test_login_success(username, password, authcode, exceptedText, inLoginModule: LoginPage):
    print("测试登录")

    inLoginModule.login(username, password, authcode)
    inLoginModule.wd.implicitly_wait(10)

    propmt = inLoginModule.wd.find_element(by=By.XPATH, value="//p[@class='el-message__content']")
    inLoginModule.wd.implicitly_wait(5)

    # 判断是否登录成功
    assert propmt.text == exceptedText


@allure.title("测试登录错误")
@allure.description("所有登录错误的场景")
@pytest.mark.parametrize('username, password, authcode, exceptedText',[
    ('admin123', '123456', '123456', '账户名或密码错误'),
    # ('admin', '123456', '123456', '系统接口请求超时')
])
def test_login_error(username, password, authcode, exceptedText, inLoginModule: LoginPage):
    print("测试登录")

    inLoginModule.login(username, password, authcode)
    inLoginModule.wd.implicitly_wait(10)

    propmt = inLoginModule.wd.find_element(by=By.XPATH, value="//p[@class='el-message__content']")
    inLoginModule.wd.implicitly_wait(5)

    # 判断是否登录成功
    assert propmt.text == exceptedText





