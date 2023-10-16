
from enum import Enum
import pytest

class CMSURL(Enum):

    # 登录页
    LOGIN = "login?redirect=/index"

    # 新增组件
    COMPONENT = "add/component"

