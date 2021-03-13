import re
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



	## Метод теста всегда должен начинаться с фразы test!
	def test_search_at_yandex_ru(self):

		## Создание ссылки на объект драйвера (смотри SetUp)
		browser = self.browser
		## Примечание: драйвер будет ждать пока страница не загрузится (событие "onload" игнорируется!)
		browser.get('http://www.yandex.ru')
		## Проверка содержит ли заголовок слово "Яндекс"
		self.assertIn('Яндекс', browser.title)

		elem = browser.find_element_by_name('text')
		## Ввод текста в найденное поле "text"
		elem.send_keys('Тензор')


		time.sleep(2)
		locator = (By.XPATH, '/html/body/div[3]') # просто пример, необходимо вставить свое значение
		wait = WebDriverWait(browser, 2)
		elements = wait.until(EC.visibility_of_element_located(locator))
		#self.assert_(), 'Таблица с подсказками не доступна!'
		print(type(elements))


		## Импорт из "selenium.webdriver.common.keys"
		elem.send_keys(Keys.ENTER) 
		## Проверка того, получили ли мы какой либо результат
		assert "No results found." not in browser.page_source
		time.sleep(3)	


		'''
			Парсит ВСЕ ссылки на страничке
		elems = browser.find_elements_by_xpath("//a[@href]")
		for elem in elems:
			print(elem.get_attribute("href"))
		'''