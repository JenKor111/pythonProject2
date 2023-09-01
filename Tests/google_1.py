import time

from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser, config


browser.open('https://www.google.com/');
time.sleep(5)
browser.element(by.name('q')).type('Магазин алло').press_enter()
time.sleep(5)
browser.all('.LC20lb')[2].click()
time.sleep(5)
page_text = browser.driver.page_source.lower()
count = page_text.count('алло')
print('Слово алло повторюється на сторінці:', count, 'разів')
