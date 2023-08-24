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
    print("Тест не пройшов. Знайдено {len(github_links)} посилання(ь).")


# Закриття веб-драйвера
driver.quit()

