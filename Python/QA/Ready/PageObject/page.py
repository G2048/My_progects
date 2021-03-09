from element import BasePageElement
from locators import MainPageLocators

class SearchTextElement(BasePageElement):
    """Этот класс получает поисковый текст из указанного локатора"""

    #Локатор для окна поиска, в которое вводится строка поиска.
    locator = 'text'


class BasePage(object):
    """Базовый класс для инициализации базовой страницы, которая будет вызываться со всех страниц"""

    def __init__(self, browser):
        self.browser = browser


class MainPage(BasePage):
    """Здесь находятся методы действий на домашней странице. Т.е. Python.org"""

    #Объявляет переменную, которая будет содержать полученный текст
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Проверяет, присутствует ли жестко запрограммированный текст «Python» в заголовке страницы."""
        return "Яндекс" in self.browser.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.browser.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Здесь находятся методы действий на странице результатов поиска"""

    def is_results_found(self):
        # Вероятно, следует искать этот текст в конкретном элементе страницы 
        # но на данный момент он работает нормально
        return "No results found." not in self.browser.page_source