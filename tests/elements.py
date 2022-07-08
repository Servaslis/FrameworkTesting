import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TestShit():
    def test_1(self, driver):
        page = BasePage(driver, 'https://google.com')
        page.open()
        element = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a')
        assert 'Почта' in element.text
        time.sleep(1)

    def test_2(self, driver):
        page = BasePage(driver, 'https://google.com')
        page.open()
        element = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a')
        assert 'Поhта' in element.text, 'eat shet test'
        time.sleep(1)

    def test_3(self, driver):
        page = BasePage(driver, 'https://google.com')
        page.open()
        element = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a')
        assert 'Поeта' in element.text, 'not passed'
        time.sleep(1)
