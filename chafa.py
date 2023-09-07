import time

from selene import Browser, by
from selene.support.shared import browser, config
from selene.support.conditions import be

config.window_width = 1920
config.window_height = 1080

#Пошуковий запит гугл
browser.open('https://www.google.com/');
time.sleep(2)
browser.element(by.name('q')).type('магазин шафа').press_enter()
time.sleep(2)
#Перехід по 1му результату
browser.all('.LC20lb')[0].click()
time.sleep(2)
#Авторизація
browser.element('[href="/uk/login"]').click()
time.sleep(2)
browser.element('[name="username"]').type('evgeniyaaaaaa007').press_enter()
browser.element('[name="password"]').type('Q@123456').press_enter()
time.sleep(2)
browser.element('.vFhB6yaBSu_LOrFZyXUr').press_enter()
#Знаходження товару
browser.element('[name="search_text"]').type('пухове пальто').press_enter()
time.sleep(5)
browser.element('[href="/uk/women/verhnyaya-odezhda/puhoviki/131229609-puhove-palto-z-hutrom-chorno-buroyi-lisici?from-adv=true"]').click()
#додавання в кошик
browser.element('.vFhB6yaBSu_LOrFZyXUr.IR7CcsmoykX4NQzvgGCt.ZhFAwoZUgtFYw9M1SNDv').click()
time.sleep(5)
#Редагування кількості і видалення
browser.element('[class="vFhB6yaBSu_LOrFZyXUr elUm1FXWrtyJt0afwHkk l8dvmdA19kSQoAuZ3AQF"]').click()
time.sleep(2)
browser.element('.k5BhJYMJMTSEiW_ZP77D').click()
time.sleep(2)


