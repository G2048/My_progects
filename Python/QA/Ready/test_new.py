from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdr
iver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import re


class YandexRuSearch(unittest.TestCase):
	"""This is test created for testing Yandex Ru Search"""

	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.maximize_window()


	def test_search_at_yandex_ru(self):
		browser = self.browser
		browser.get('http://www.yandex.ru')
		self.assertIn('Яндекс', browser.title)
		wait = WebDriverWait(browser, 3)

		elem = browser.find_element_by_name('text')
		elem.send_keys('Тензор')

		# Получаем локатор всплывающей подсказки, тем самым проверяя ее наличие
		locator = (By.CSS_SELECTOR, '.mini-suggest__popup_visible')
		wait.until(EC.visibility_of_element_located(locator))

		elem.send_keys(Keys.ENTER)
		#time.sleep(3)

		for i in range(1,6):
			reference = browser.find_element_by_xpath('//*[@id="search-result"]/li[{}]//a'.format(i))
			link = reference.get_attribute('href')
			if re.match( r'https://tensor.ru', link):
				print("Page is number {} have adress of \"tensor.ru\"! url: {}".format(i, link))
			else:
				print('Page is number {} haven\'t adress of "tensor.ru"! url: {}'.format(i, link))

		## Проверка того, получили ли мы какой либо результат
		assert "No results found." not in browser.page_source


	def test_search_images_at_yandex_ru(self):
		browser = self.browser
		browser.get('https://yandex.ru')
		assert 'Яндекс' in browser.title
		wait = WebDriverWait(browser, 5)
  
		images = browser.find_element_by_link_text('Картинки')
		images.click()
		#images = (By.CSS_SELECTOR, '.home-link_black_yes')
		#wait.until(EC.element_to_be_clickable(images))

		tabs = browser.window_handles
		browser.switch_to.window(tabs[1])

		if re.match(r'https://yandex.ru/images/', browser.current_url):
			print('The correct page is open')
		else:
			print('The incorecct page is open')
			#browser.quit()

		img = (By.CLASS_NAME, 'serp-item__link')
		print(len(img))
		for i in range(len(img)):
			print(img[i])
		wait.until(EC.elements_to_be_clickable(img[1]))

		img_link = (By.NAME,'href')
		wait.until(EC.element_to_be_clickable(img_link))

		text_in_placeholder = (By.XPATH, '/html/body/header/div/div[1]/div[2]/form/div[1]/span/span/input')
		wait.until(EC.element_to_be_clickable(text_in_placeholder))
		self.assertEqual(img, text_in_placeholder), "WE ARE WRONG PAGE JO!!! (Texts from placeholders not equal!)" 

		## Получение СПИСКА! (elementS!!!) доступных картинок!!!
		img_1 = browser.find_elements_by_class_name('serp-item__link')
		img_link = img_1[0].get_attribute('href')
		browser.get(img_link)

		## Так как кнопка картинки прогружается не сразу поставим функцию "ожидание":
		button = (By.PARTIAL_LINK_TEXT, 'Открыть')
		element = wait.until(EC.element_to_be_clickable(button))

		self.assertIn(text_in_placeholder, browser.title),  'Image wasnt opened!!!'
		#time.sleep(3)

		url_image_before = browser.title
		#wait.until(EC.element_to_be_clickable(url_image_before))

		## ИЩЕМ ДУРАЦКИЕ КНОПКИ ЯНДЕКСА!
		button_next = (By.XPATH, '/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[4]/i')
		wait.until(EC.element_to_be_clickable(button_next))
		button_back = (By.XPATH, '/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[1]/i')
		wait.until(EC.visibility_of_element_located(button_back))
		print(str(button_back.is_displayed()))

		url_image_after = browser.title
		# Сравниваем текущий url и первой картинки, тем самым удостоверяясь что мы вернулись на первую картинку
		self.assertEqual(
			url_image_before, url_image_after), "These are not the droids you are looking for!!! (Imagenes is not equal =__=)"

		## Закрываем окно картинки:
		#browser.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[2]').click()
		exit_button = (By.XPATH, '/html/body/div[14]/div[1]/div/div/div[2]')
		wait.until(EC.element_to_be_clickable(exit_button))

	def tearDown(self):
		self.browser.quit() 
		"Run test is finished! YHY!"
		#time.sleep(5)


if __name__ == "__main__":
	unittest.main(verbosity = 1)
	#suite = unittest.TestLoader().loadTestsFromTestCase(YandexRuSearch)
	#unittest.TextTestRunner(verbosity=1).run(suite)
