from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
#browser.maximize_window()
## Вводим url:
browser.get('https://yandex.ru')

## Ищем окно ввода:
search = browser.find_element_by_id('text')

## Вводим слово "Тензор" в поле ввода и жмем "Enter":
search.send_keys('Тензор')
search.send_keys(Keys.ENTER)

## Находим поле текста "Картинки" и кликаем по нему:
browser.find_element_by_link_text('Картинки').click()

## Так как селениум думает, что мы на первой вкладке, нужно указать что недо работать на второй странице:
### Получаем список активных вкладок:
tabs = driver.window_handles

## Переходим на вторую вкладку:
browser.switch_to.window(tabs[1])

img_1 = browser.find_element_by_class_name()


time.sleep(5)
browser.quit()

