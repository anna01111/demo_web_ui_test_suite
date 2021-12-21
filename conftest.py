from pytest import fixture
from selenium import webdriver


@fixture
def browser():
    browser = webdriver.Chrome()
    return browser

