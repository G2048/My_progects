import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
## Импортирование для работы свыпадающими списками
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
#browser.maximize_window()
browser.get('https://pk.mipt.ru/bachelor/list/')

## Поиск элемента в выпадающем окне:
for_choise = browser.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[3]/div[2]/select')
## Выбор элемента из выпадающего списка по видимому тексту:
Select(for_choise).select_by_visible_text('Общий конкурс')

## Или выбор по значению:
#Select(for_choise).select_by_value()

for_choise = browser.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')
## Выбор элемента из выпадающего списка по значению:
Select(for_choise).select_by_value('1')

for_choise = browser.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')
Select(for_choise).select_by_value('250')

for_choise = browser.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[6]/div[2]/select')
Select(for_choise).select_by_value('2')

#find_the_button = browser.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[1]/div/div')
find_the_button = browser.find_element_by_text('Применить')
## Кликнуть на найденную кнопку:
find_the_button.click()

time.sleep(3)

## Получение ТЕКУЩЕГО html кода страницы:
html = browser.page_source


import pandas as pd
df = pd.read_html(html)
print(df[0])

time.sleep(5)
browser.close()

