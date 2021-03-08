import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

## Вводим url:
browser.get('https://yandex.ru')
assert 'Яндекс' in browser.title

## Ищем окно ввода:

## Поиск окна ввода по id:
#search = browser.find_element_by_id('text')

## Находим поле текста "Картинки" и кликаем по нему:
images = browser.find_element_by_link_text('Картинки')
#if 'Картинки' in images:
images.click()
#else:
#	print("Элемент '{}' не найден!".format("Картинки"))
	#browser.quit()


## Так как селениум думает, что мы на первой вкладке, нужно указать что недо работать на второй странице:
### Получаем список активных вкладок:
tabs = browser.window_handles

## Переходим на вторую вкладку:
tab_2 = browser.switch_to.window(tabs[1])
time.sleep(2)

#print(browser.current_url)
if re.match(r'https://yandex.ru/images/', browser.current_url):
	print('Открыта верная страница!')
else:
	print('Открыта не верная страница!')
	#browser.quit()

img = browser.find_element_by_class_name('PopularRequestList-SearchText')
img.click()
time.sleep(3)

search = browser.find_element_by_name('text')
## Очистка поля ввода:
search.clear()

search.send_keys('блюда из тыквы')
search.send_keys(Keys.ENTER)
time.sleep(2)

## Получение СПИСКА! (elementS!!!) доступных картинок!!!
img_1 = browser.find_elements_by_class_name('serp-item__link')

## Для получения [второй] картинки.... Находим аттрибут 'hyper reference':
img_link = img_1[0].get_attribute('href')
browser.get(img_link)

## Так как кнопка картинки прогружается не сразу поставим функцию "ожидание":
wait = WebDriverWait(browser, 3)
## Для определенного элемента задаем "ожидание", пока не найдется нужный элемент
element = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Открыть')))
# browser.find_element_by_partial_link_text('Открыть').click() - НЕ РАБОТАЕТ!!!

## ИЩЕМ ДУРАЦКИЕ КНОПКИ ЯНДЕКСА!
time.sleep(3)
button_next = browser.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[4]/i')
button_next.click()

time.sleep(3)
button_back = browser.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[1]/i')
button_back.click()

## Закрываем окно картнки:
browser.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[2]').click()

## Любуемся полученной красотой:))
time.sleep(5)
browser.quit()



