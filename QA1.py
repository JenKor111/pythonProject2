import time

from selene import Browser, by
from selene.support.shared import browser
from selene.support.conditions import be

def test_open_friends():
    browser.open('http://opencart.qatestlab.net/')
    time.sleep(5)
    browser.element('#stuck > div > div > div > div > div > div > div > div > ul > li:nth-child(10) > a').click()
    time.sleep(5)
    browser.element('#content > div > div:nth-child(1) > div > a').click()
    time.sleep(5)
    browser.element('#input-firstname').type('Женя').press_enter()
    time.sleep(5)
    browser.element('#input-lastname').type('123').press_enter()
    time.sleep(5)
    browser.element('#input-email').type('evgeniyaakornienko@gmail.com').press_enter()
    time.sleep(3)
    browser.element('#input-telephone').type('0969212652').press_enter()
    time.sleep(3)
    browser.element('#input-password').type('123456').press_enter()
    time.sleep(3)
    browser.element('#input-confirm').type('123456').press_enter()
    time.sleep(5)
    browser.element(by.css('[type="radio"][name="agree"]')).click()
    time.sleep(5)
    browser.element(by.css('[value="Продолжить"]')).click()
    time.sleep(5)

def test_authorization():
    browser.open('http://opencart.qatestlab.net/')
    time.sleep(5)
    browser.element('#stuck > div > div > div > div > div > div > div > div > ul > li:nth-child(10) > a').click()
    time.sleep(5)
    browser.element('#input-email').type('evgeniyaakornienko@gmail.com').press_enter()
    time.sleep(3)
    browser.element('#input-password').type('123456')
    time.sleep(3)
    browser.element(by.css('[value="Войти"]')).click()
    time.sleep(5)

def test_search():
    browser.open('http://opencart.qatestlab.net/')
    time.sleep(5)
    browser.element('[name="search"]').type('Popamazing')
    time.sleep(5)
    browser.element('#search > button').click()
    time.sleep(5)
    search_results_text = browser.all('.product-layout')
    assert len(search_results_text) > 0, 'No found'

def test_shopping_cart():
    browser.open('http://opencart.qatestlab.net/')
    time.sleep(5)
    browser.element('[href="http://opencart.qatestlab.net/index.php?route=product/category&path=31"]').click()
    time.sleep(5)
    browser.element('[href="http://opencart.qatestlab.net/index.php?route=product/product&path=31&product_id=34"]').click()
    time.sleep(5)
    browser.element('[href="#tab-specification"]').click()
    time.sleep(5)
    browser.element('#button-cart.btn-primary').click()
    time.sleep(5)
    browser.element('.counter.counter-plus.material-design-add186').click()
    time.sleep(5)

