import pytest
import math
import time
from selenium import webdriver

def test_should_be_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert button, "The page does not contain an add to cart button"    
    time.sleep(5)
