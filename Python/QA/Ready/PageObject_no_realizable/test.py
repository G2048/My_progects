import unittest
from selenium import webdriver
import page

class YandexRuSearch(unittest.TestCase):
    """This is test created for testing Yandex Ru Search"""

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://www.yandex.ru')
        self.assertIn('Яндекс', self.browser.title)
        self.browser.maximize_window()

    def test_search_tenzor_at_yandex_ru(self):

        #Загрузите главную страницу. В этом случае домашняя страница Python.org.
        main_page = page.MainPage(self.browser)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "Мы не на Яндексе!"

        #Устанавливает текст текстового поля поиска на "pycon"
        main_page.search_text_element = "Тензор"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.browser)
        
        #Проверяет, что страница результатов не пуста
        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        ## "close" - закрывает одну вкладку, а "quit" - закроет браузер полностью   
        self.browser.quit() 
        print("Прогон теста завершен!")

if __name__ == "__main__":
    unittest.main()