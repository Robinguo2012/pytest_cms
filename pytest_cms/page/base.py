from selenium import webdriver


def singleton(cls):
    instance = {}

    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper

@singleton
class CMSUtils:
    
    def __init__(self, url) -> None:
        print("=====生成driver 函数执行===")
        self.base_url = url

        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        
        self.wd = webdriver.Chrome(options=options)
        self.wd.implicitly_wait(10)
        

class BasePage:
    
    def __init__(self, utils:CMSUtils):
        self.wd = utils.wd
        self.utils = utils
    
    def open_url(self,url):
        self.utils.wd.get(f'{self.utils.base_url}{url}')