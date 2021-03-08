from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.get('https://yandex.ru')

## Поиск окна ввода по id:
search = browser.find_element_by_id('text')

search.send_keys('блюда из тыквы')
search.send_keys(Keys.ENTER)

## Переключение в "Картинки"
browser.find_element_by_partial_link_text('Картинки').click()

## Получение списка открытых вкладок
tabs = browser.window_handles

## Переключаемся на 2-ю вкладку
browser.switch_to.window(tabs[1])

## Получение СПИСКА! (elementS!!!) доступных картинок!!!
img_1 = browser.find_elements_by_class_name('serp-item__link')

## Для получения [второй] картинки.... Находим аттрибут 'hyper reference' :
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

browser.quit()