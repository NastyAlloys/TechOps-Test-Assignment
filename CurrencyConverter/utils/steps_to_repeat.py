from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest
import allure
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

class StartEnd:
    #открыть браузер, загрузить страницу
    def setup_class(self):
        # self.driver = webdriver.Firefox(executable_path=r'C:/Utility/BrowserDrivers/geckodriver.exe')
        self.driver = webdriver.Chrome(executable_path=r'C:/Utility/BrowserDrivers/chromedriver.exe')
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get('http://www.sberbank.ru/ru/quotes/converter')
        print(self.driver.title)
        with pytest.allure.step('Загрузка страницы'):
            assert 'Калькулятор иностранных валют' in self.driver.title, 'Страница не загрузилась'

    #закрыть браузер
    def teardown_class(self):
        self.driver.quit()

class Driver:
    def __init__(self, driver):
        self.driver = driver

class Converter(Driver):
    #найти элемент
    def find(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    #ввод суммы и конвертация
    # TODO: дописать функцию проверки на ввод данных
    # def input_field_func(self, input, output):

    #проверить список валют "из"
    def from_currency_func(self, data):
        #находим и кликаем список валюты
        currency_div = self.driver.find_element_by_class_name("rates-aside__filter-block-line_field_converter-from")
        currency_field = currency_div.find_element_by_class_name("rates-aside__filter-block-line-right")
        currency_field.click()
        
        with pytest.allure.step('Выбор валюты из списка'):
            #находим валюту в списке и выбираем ее
            currency_item = currency_field.find_element_by_xpath("//div[@class='select opened']//div[@class='visible']/*[contains(text()," + " '" + data + "'" + ")]")
            currency_item.click()
            WebDriverWait(self.driver, 3)
            currency_text = currency_field.find_element_by_css_selector('strong').text
            return currency_text

    # Проверить список валют "в"
    # TODO: написать верный XPath, так как по непонятной причине логика верстки для валюты "в" отличается от верстки для валюты "из", где в названии класса присутствует "_converter-from"
    # def to_currency_func(self, data):
        #находим и кликаем список валюты

        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@class='converterTo']")))
        # to_currency_select = self.driver.find_element_by_xpath("//select[@class='converterTo']")
        # to_currency = to_currency_select.find_element_by_xpath("..")
        # to_currency.click()