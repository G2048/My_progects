import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class YandexRuSearch(unittest.TestCase):
	"""docstring for YandexRuSearch"""
	## Настройка обращения драйвера к браузеру
	def setUp(self): 
		self.driver = webdriver.Chrome() 
	## Метод теста всегда должен начинаться с фразы test!
	def test_search_in_yandex_ru(self):
		## Создание ссылки на объект драйвера (смотри SetUp)
		driver = self.driver
		## Примечание: драйвер будет ждать пока страница не загрузится (событие "onload" игнорируется!)
		driver.get('http://www.yandex.ru')
		## Проверка содержит ли заголовок слово "Яндекс"
		self.assertIn('Яндекс', driver.title)

		elem = driver.find_element_by_name('text')
		## Ввод текста в найденное поле "text"
		elem.send_keys('Тензор') 
		elem.send_keys(" and some", Keys.ARROW_DOWN)
		## Импорт из "selenium.webdriver.common.keys"
		elem.send_keys(Keys.ENTER) 
		## Проверка того, получили ли мы какой либо результат
		assert "No results found." not in driver.page_source 
	# Вызывается после каждого метода теста
	def tearDown(self):
		## "close" - закрывает одну вкладку, а "quit" - закроет браузер полностью	
		self.driver.close() 

if __name__ == "__main__":
	unittest.main(verbosity = 1)