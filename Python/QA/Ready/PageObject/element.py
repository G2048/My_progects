from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    """Базовый класс страницы, который инициализируется для каждого класса объекта страницы."""

    def __set__(self, obj, value):
        """Устанавливает текст в указанное значение"""
        browser = obj.browser
        WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_name(self.locator))
        browser.find_element_by_name(self.locator).clear()
        browser.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Получает текст указанного объекта"""

        browser = obj.browser
        WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_name(self.locator))
        element = browser.find_element_by_name(self.locator)

        return element.get_attribute("value")