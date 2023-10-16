import pytest

def pytest_addoption(parser):
    """"添加一个命令行选项"""
    parser.addoption(
        "--env", default="local", choices=["local", "dev", "pre"], help="enviroment parameter")

    
@pytest.fixture(scope="session")
def get_env(request):
    return request.config.getoption("--env")