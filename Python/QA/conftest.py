from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://www.yandex.ru')
assert 'Яндекс' in driver.title

elem = driver.find_element_by_name('text')
elem.send_keys('Тензор')
#elem.clear()

element = driver.find_elements_by_xpath("//select[@name='name']")
all_options = driver.find_elements_by_tag_name("option")

for option in all_options:
	print("Value is: %s" % option.get_attribute("value"))
	option.click()

#elem.send_keys(" and some", Keys.ARROW_DOWN)
#elem.send_keys(Keys.ENTER)

assert "No results found." not in driver.page_source

#driver.close()