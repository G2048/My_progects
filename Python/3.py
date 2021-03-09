import re
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class YandexRuSearch(unittest.TestCase):
	"""This is test created for testing Yandex Ru Search"""

	## Настройка обращения драйвера к браузеру
	def setUp(self): 
		self.browser = webdriver.Chrome()

	## Метод теста всегда должен начинаться с фразы test!
	def test_search_tenzor_at_yandex_ru(self):

		## Создание ссылки на объект драйвера (смотри SetUp)
		browser = self.browser
		## Примечание: драйвер будет ждать пока страница не загрузится (событие "onload" игнорируется!)
		browser.get('http://www.yandex.ru')
		## Проверка содержит ли заголовок слово "Яндекс"
		self.assertIn('Яндекс', browser.title)

		elem = browser.find_element_by_name('text')
		## Ввод текста в найденное поле "text"
		elem.send_keys('Тензор') 

		## Импорт из "selenium.webdriver.common.keys"
		elem.send_keys(Keys.ENTER) 
		## Проверка того, получили ли мы какой либо результат
		assert "No results found." not in browser.page_source
		time.sleep(3)	

	

if __name__ == "__main__":
	#unittest.main(verbosity = 1)
	suite = unittest.TestLoader().loadTestsFromTestCase(YandexRuSearch)
	unittest.TextTestRunner(verbosity=1).run(suite)