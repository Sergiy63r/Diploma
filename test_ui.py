import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from class_ui import Kinopoisk

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # noqa: E501
browser.get('https://www.kinopoisk.ru')
ui = Kinopoisk(browser)


@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Поиск филма по названию")
def test_poisk():
    names = 'Реквием по мечте'
    ui.poisk_film(names)


@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Ввод названия фильма")
def test_input():
    names = 'Sloum'
    ui.input_name(names)


@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Воспроизведение трейлера")
def test_play():
    ui.play_trayler()


@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Авторизация")
def test_avtoriz():
    login = "sergeyQA58.0@yandex.ru"
    passwd = "formula163!QAM"
    ui.avtorizacia(login, passwd)
