import pytest
import allure


if __name__ == '__main__':
    pytest.main(["-m error", "-s", r"--alluredir=report\allure"])




