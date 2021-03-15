from selenium.webdriver.support import expected_conditions as EC
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

		# Getting location popup hint to check what we found it
		locator = (By.CSS_SELECTOR, '.mini-suggest__popup_visible')
		wait.until(EC.visibility_of_element_located(locator))

		elem.send_keys(Keys.ENTER)

		for i in range(1,6):
			reference = browser.find_element_by_xpath('//*[@id="search-result"]/li[{}]//a'.format(i))
			link = reference.get_attribute('href')
			if re.match( r'https://tensor.ru', link):
				print("Page is number {} have adress of \"tensor.ru\"! url: {}".format(i, link))
			else:
				print('Page is number {} haven\'t adress of "tensor.ru"! url: {}'.format(i, link))

		# Checking if we got any result
		assert "No results found." not in browser.page_source


	def test_search_images_at_yandex_ru(self):
		browser = self.browser
		browser.get('https://yandex.ru')
		assert 'Яндекс' in browser.title
		wait = WebDriverWait(browser, 10)
		# Clicking into "images"
		images = (By.PARTIAL_LINK_TEXT, 'Картинки')
		wait.until(EC.element_to_be_clickable(images)).click()

		tabs = browser.window_handles
		browser.switch_to.window(tabs[1])
		# Verification
		if re.match(r'https://yandex.ru/images/', browser.current_url):
			print('The correct page is open')
		else:
			print('The incorecct page is open')
			#browser.quit()
		# Finding text from the first popular image
		text_from_first_popular_image = browser.find_element_by_xpath(
			'/html/body/div[6]/div[1]/div[1]/div/div/div[1]/div[1]/a')
		text = text_from_first_popular_image.get_attribute('text')
   
		# Finding of The first popular image
		img = (By.CLASS_NAME, 'PopularRequestList-SearchText')
		wait.until(EC.element_to_be_clickable(img)).click()
  
		# Opening the first page of popular images
		img_link = (By.CLASS_NAME, 'serp-item__link')
		wait.until(EC.element_to_be_clickable(img_link)).click()
		# Finding of element "text" from the search window
		text_in_title = browser.find_element_by_xpath('/html/body/header/div/div[1]/div[2]/form/div[1]/span/span/input').get_attribute('value')
		# text_in_title = browser.page_source # Interesting is function
		self.assertEqual( text_in_title, text ), "WE ARE ON THE WRONG PAGE JO!!! (Text from the search list is wronger!)"
  
		first_image = (By.CLASS_NAME, 'serp-item__link')
		wait.until(EC.element_to_be_clickable(first_image))

		# We finding the list of an (elementS!!!) avalible pictures
		img_1 = browser.find_elements_by_class_name('serp-item__link')
		img_link = img_1[0].get_attribute('href')

		self.assertIn(text_in_title, browser.title),  'Another Image is opened!!!'

		# Getting url for further checking
		url_image_before = browser.current_url
		# LOKING FOR THE STUPID YANDEX BUTTON!
		button_next = (
			By.XPATH, '/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[4]')
		wait.until(EC.presence_of_element_located(button_next)).click()

		button_back = (
			By.XPATH, '/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[1]')
		wait.until(EC.presence_of_element_located(button_back)).click()

		# We are comparing a before url with after
		url_image_after = browser.current_url
		self.assertEqual(url_image_before, url_image_after), "These are not the droids you are looking for!!! (Images is not equal =__=)"

		# Closing the image window
		exit_button = (By.XPATH, '/html/body/div[14]/div[1]/div/div/div[2]')
		wait.until(EC.element_to_be_clickable(exit_button)).click()

	def tearDown(self):
		self.browser.quit() 
		"Run test is finished! YHY!"



if __name__ == "__main__":
	unittest.main(verbosity = 1)
	#suite = unittest.TestLoader().loadTestsFromTestCase(YandexRuSearch)
	#unittest.TextTestRunner(verbosity=1).run(suite)
