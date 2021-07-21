import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    return webdriver.Chrome(executable_path=".\\drivers\\chromedriver.exe")

# @pytest.fixture()
# def setup(request):
#     request.cls.driver = webdriver.Chrome(executable_path="D:\\MyWorkSpace\\Python-Selenium\\softwares\\chromedriver.exe")