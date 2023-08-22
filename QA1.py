from selenium import webdriver
from selenium.webdriver.common.by import By


# Ініціалізація веб-драйвера (в даному випадку, Chrome)
driver = webdriver.Chrome()

# Відкриття сторінки Ecosia
driver.get("https://www.ecosia.org/")

# Знаходження поля пошуку і введення тексту
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys("yashaka selene")

# Натискання клавіші Enter для пошуку
search_input.submit()

# Очікування знаходження результатів пошуку
driver.implicitly_wait(10)

# Клік по першому посиланню у результатах пошуку
first_link = driver.find_element(By.CSS_SELECTOR, "div.result__title")
first_link.click()


# Перевірка наявності трьох посилань на https://github.com/yashaka/selene
# github_links = driver.find_elements(By.CSS_SELECTOR, "a[href='/yashaka/selene']")
github_links = driver.find_elements(By.LINK_TEXT, "selene")

if len(github_links) == 3:
    print("Тест пройшов успішно. Знайдено 3 посилання.")
else:
    print(f"Тест не пройшов. Знайдено {len(github_links)} посилання(ь).")

# Закриття веб-драйвера
driver.quit()

import time

from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser

browser.open('https://todomvc.com/examples/emberjs/#/');

browser.element('#new-todo').type('тобі').press_enter()
browser.element('#new-todo').type('привіт').press_enter()
browser.element('#new-todo').type('пока').press_enter()
browser.all('#todo-list>li').should(have.exact_texts('тобі', 'привіт', 'пока'))

browser.element('#todo-list>li:nth-of-type(2) .toggle').click()
browser.all('#todo-list>li.completed').should(have.texts('привіт'))
browser.all('#todo-list>li:not(.completed)').should(have.exact_texts('тобі', 'пока'))

browser.element(by.text('Completed')).click()

browser.element('#ember9').click()
browser.element('#ember8').click()


browser.quit()