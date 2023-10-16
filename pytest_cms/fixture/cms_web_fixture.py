import pytest
import yaml
from pytest_cms.page.base import CMSUtils
from pytest_cms.config import SETTING_YMAL_DIR
import os

@pytest.fixture(scope='session')
def get_cmsUtils(get_env)-> CMSUtils:
     with open(os.path.join(SETTING_YMAL_DIR, f'{get_env}_env.yml'), encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return CMSUtils(url=data['host'])

