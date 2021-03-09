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

		## Импорт из "selenium.webdriver.common.keys"
		elem.send_keys(Keys.ENTER) 
		## Проверка того, получили ли мы какой либо результат
		assert "No results found." not in browser.page_source
		time.sleep(3)	

	## Метод теста всегда должен начинаться с фразы test!
	def test_search_images_at_yandex_ru(self):
		browser = self.browser

		browser.maximize_window()

		browser.get('https://yandex.ru')
		assert 'Яндекс' in browser.title
		## Находим поле текста "Картинки" и кликаем по нему:
		images = browser.find_element_by_link_text('Картинки')
		images.click()

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

		img = browser.find_elements_by_xpath('/html/body/div[6]/div[1]/div[1]/div/div/div[1]/div[1]/a')
		img_link_1= img[0].get_attribute('href') # Получаем url картинки!!!
		browser.get(img_link_1)
		time.sleep(3)

		now_url = browser.current_url # Получаем текущий url
		# Сравниваем текущий url и картинки, тем самым удостоверяясь что в поиске верный текст
		self.assertEqual(now_url,img_link_1), "Мы не на той странице Джо!!!" 

		## Получение СПИСКА! (elementS!!!) доступных картинок!!!
		img_1 = browser.find_elements_by_class_name('serp-item__link')
		## Для получения [первой] картинки.... Находим аттрибут 'hyper reference':
		img_link = img_1[0].get_attribute('href')
		browser.get(img_link)

		## Так как кнопка картинки прогружается не сразу поставим функцию "ожидание":
		wait = WebDriverWait(browser, 3)
		## Для определенного элемента задаем "ожидание", пока не найдется нужный элемент
		element = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Открыть')))
		# browser.find_element_by_partial_link_text('Открыть').click() - НЕ РАБОТАЕТ!!!

		## ИЩЕМ ДУРАЦКИЕ КНОПКИ ЯНДЕКСА!
		time.sleep(3)
		now_url_before= browser.current_url # Получаем текущий url первой открытой картинки
		button_next = browser.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[4]/i')
		button_next.click()

		time.sleep(1)
		button_back = browser.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[1]/i')
		button_back.click()

		time.sleep(1)
		now_url_after = browser.current_url # Получаем текущий url

 		# Сравниваем текущий url и первой картинки, тем самым удостоверяясь что мы вернулись на первую картинку
		self.assertEqual(now_url_before,now_url_after), "Это не те дроиды что вы ищете!!!(Изображения не совпадают =__=)"

		## Закрываем окно картнки:
		browser.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[2]').click()

		## Любуемся полученной красотой:))
		time.sleep(5)

if __name__ == "__main__":
	unittest.main(verbosity = 1)
	#suite = unittest.TestLoader().loadTestsFromTestCase(YandexRuSearch)
	#unittest.TextTestRunner(verbosity=1).run(suite)