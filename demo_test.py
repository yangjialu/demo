import pytest


@pytest.fixture()
def init_web():
    print("初始化浏览器")
    yield
    print("退出浏览器")


@pytest.fixture(scope="session")
def session_web():
    print("session before")
    yield
    print("session after")


@pytest.fixture(scope="class")
def class_web():
    print("class before")
    yield
    print("class after")


@pytest.fixture(scope="module")
def module_web():
    print("module before")
    yield
    print("module after")


@pytest.mark.q
def test_demo(init_web, class_web, module_web, session_web):
    print("执行测试用例")

# 重运行 pytest_rerunfailures
# 命令：pytest --reruns 2 --reruns-delay 5