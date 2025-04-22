import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Kinopoisk():
    def __init__(self, browser):
        self.browser = browser
        self.browser.maximize_window()
        self.browser.implicitly_wait(20)

    @allure.step("Вводим имя {names}")
    def poisk_film(self, names: str):
        """
           Поиск фильма по названию.
           Можно указывать часть названия, если не помните полное.
           Поиск будет произведён и вам откроется список фильмов
           в которых будет присутствовать часть введённого низания.
        """
        poisk = self.browser.find_element(By.CSS_SELECTOR, "input[name='kp_query']")    # noqa: E501
        poisk.send_keys(names, Keys.RETURN)

    @allure.step("Вводим имя {names}")
    def input_name(self, names: str):
        """
           Здесь мы проверяем отображение в поисковой строке ввод:
           букв, цифр, символов.
           Открываться сылки и куда-то переходить мы не должны.
        """
        poi = self.browser.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]')    # noqa: E501
        poi.send_keys(names)

    @allure.step("Запустить трейлер для просмотра")
    def play_trayler(self):
        self.browser.find_element(By.CSS_SELECTOR, '[class="pic"]').click()
        self.browser.find_element(By.CSS_SELECTOR, '[class="styles_fade__bfTU2"]').click()    # noqa: E501

    @allure.step("Авторизуемся")
    def avtorizacia(self, login: str, passwd: str):
        self.browser.get('https://passport.yandex.ru/auth/add/login?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252F%26uuid%3D8417c1ba-4e6f-4c76-8245-a8311802e466')    # noqa: E501
        self.browser.find_element(By.CSS_SELECTOR, 'input[data-t="field:input-login"]').send_keys(login, Keys.RETURN)       # noqa: E501
        self.browser.set_page_load_timeout(10)
        self.browser.find_element(By.CSS_SELECTOR, 'input[data-t="field:input-passwd"]').send_keys(passwd, Keys.RETURN)     # noqa: E501
