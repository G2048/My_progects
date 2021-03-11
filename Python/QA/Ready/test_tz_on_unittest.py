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
		self.browser.maximize_window()

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

		# Получаем локатор всплывающей подсказки, темсамым проверяя ее наличие
		locator = (By.CSS_SELECTOR, '.mini-suggest__popup_visible')
		wait = WebDriverWait(browser, 3)
		elements = wait.until(EC.visibility_of_element_located(locator))

		### ENTEEERRRR!!!!!
		elem.send_keys(Keys.ENTER)
		count = 0
		time.sleep(3)
#//*[@id="search-result"]/li[5]/div/h2/a
#search-result > li:nth-child(2) > div > h2 > a
#search-result > li:nth-child(3) > div > h2 > a
#search-result > li:nth-child(4) > div > h2 > a
#search-result > li:nth-child(5) > div > div > div.wrapper__cell.wrapper__cell_type_content.clearfix > h2 > a

		'''elems = browser.find_elements_by_xpath("//a[@href]")
		for elem in elems:
			print(elem.get_attribute("href"))'''

		for i in range(2,7):
			reference = browser.find_element_by_xpath('//*[@id="search-result"]/li[{}]/div/h2/a'.format(i))
			link = reference.get_attribute('href')    # //*[@id="search-result"]/li[4]/div/div/div[2]/h2/a
			print(count, i)
			count = count + 1
			print(link)
			#browser.get(link)"""


		## Импорт из "selenium.webdriver.common.keys"
		## Проверка того, получили ли мы какой либо результат
		assert "No results found." not in browser.page_source
		time.sleep(3)	

	## Метод теста всегда должен начинаться с фразы test!
	def test_search_images_at_yandex_ru(self):

		browser = self.browser
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

		# Проверка на содержание "https://yandex.ru/images/" в текущей ссылке
		if re.match(r'https://yandex.ru/images/', browser.current_url):
			print('Открыта верная страница!')
		else:
			print('Открыта не верная страница!')
			#browser.quit()

		
		img = browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div/div/div[1]/div[1]/a')
		text_in_placeholder_0 = img.get_attribute('text') # Получаем текст с первой картинки для дальнейшего сравнения

		img_link_1= img.get_attribute('href') # Получаем url картинки!!!
		browser.get(img_link_1)

		text_in_placeholder = browser.find_element_by_xpath('/html/body/header/div/div[1]/div[2]/form/div[1]/span/span/input')
		text_in_placeholder_1 = text_in_placeholder.get_attribute('value')

		time.sleep(3)
		# Сравниваем тексты из плейсхолдеров
		self.assertEqual(text_in_placeholder_0, text_in_placeholder_1), "Мы не на той странице Джо!!! (Тексты из placeholders not equal!)" 

		## Получение СПИСКА! (elementS!!!) доступных картинок!!!
		img_1 = browser.find_elements_by_class_name('serp-item__link')
		## Для получения [первой] картинки.... Находим аттрибут 'hyper reference':
		img_link = img_1[0].get_attribute('href')
		browser.get(img_link)

		## Так как кнопка картинки прогружается не сразу поставим функцию "ожидание":
		wait = WebDriverWait(browser, 5)
		## Для определенного элемента задаем "ожидание", пока не найдется нужный элемент
		element = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Открыть')))
		# browser.find_element_by_partial_link_text('Открыть').click() - НЕ РАБОТАЕТ!!!

		# Проводим проверку того открылась ли картинка
		self.assertIn(text_in_placeholder_1, browser.title),  'Картинка не открылась!!!'
		time.sleep(3)

		# Получаем url картинки для проведения проверки
		url_image_before_0 = browser.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[3]/div/img') 
		url_image_before = url_image_before_0.get_attribute('src')

		## ИЩЕМ ДУРАЦКИЕ КНОПКИ ЯНДЕКСА!
		button_next = browser.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[4]/i')
		button_next.click()

		time.sleep(1)
		button_back = browser.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[1]/i')
		button_back.click()

		time.sleep(1)
		# Получаем url картинки для проведения проверки
		url_image_after_0 = browser.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[3]/div/img') 
		url_image_after = url_image_after_0.get_attribute('src')

 		# Сравниваем текущий url и первой картинки, тем самым удостоверяясь что мы вернулись на первую картинку
		self.assertEqual(url_image_before, url_image_after), "Это не те дроиды что вы ищете!!!(Изображения не совпадают =__=)"

		## Закрываем окно картнки:
		browser.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[2]').click()

		## Любуемся полученной красотой:))
		time.sleep(5)

	## Вызывается после каждого метода теста
	def tearDown(self):
		## "close" - закрывает одну вкладку, а "quit" - закроет браузер полностью	
		self.browser.quit() 
		print("Прогон теста окончен!")
		time.sleep(2)

if __name__ == "__main__":
	unittest.main(verbosity = 1)
	#suite = unittest.TestLoader().loadTestsFromTestCase(YandexRuSearch)
	#unittest.TextTestRunner(verbosity=1).run(suite)