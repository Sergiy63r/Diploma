import allure
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from class_ui import Kinopoisk

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # noqa: E501
ui = Kinopoisk(browser)

def test_avtoriz():
    ui.avtorizacia()

def test_poisk():
    names = 'Реквием по мечте'
    ui.poisk_film(names)

def test_input():
    names = 'Sloum'
    ui.input_name(names)

def test_play():
    ui.play_trayler()
