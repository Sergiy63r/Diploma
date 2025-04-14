import allure
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Kinopoisk():
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.kinopoisk.ru')
        self.browser.maximize_window()

# Поиск фильма по имени
    def poisk_film(self, names):
        
        poisk = self.browser.find_element(By.CSS_SELECTOR, "input[name='kp_query']")
        poisk.send_keys(names, Keys.RETURN)
        sleep(5)
#browser.quit()

# Ввод двнных
    def input_name(self, names):
        poi = self.browser.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]')
        poi.send_keys(names)
        sleep(3)

# Авторизация
    def avtorizacia(self):
        self.browser.get('https://passport.yandex.ru/auth/add/login?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252F%26uuid%3D8417c1ba-4e6f-4c76-8245-a8311802e466')
        self.browser.find_element(By.CSS_SELECTOR, 'input[data-t="field:input-login"]').send_keys("sergeyQA58.0@yandex.ru", Keys.RETURN)
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.CSS_SELECTOR, 'input[data-t="field:input-passwd"]').send_keys("formula163!QAM", Keys.RETURN)
        sleep(20)

# Запустить трейлер для просмотра
    def play_trayler(self):
        self.browser.find_element(By.CSS_SELECTOR, '[class="pic"]').click()
        self.browser.find_element(By.CSS_SELECTOR, '[class="styles_fade__bfTU2"]').click()
        sleep(20)
