import allure
from class_api import ApiKinopoisk

api = ApiKinopoisk(api_url='https://api.kinopoisk.dev')


@allure.suite("Кинопоиск API")
@allure.feature("Позитивные проверки")
@allure.epic("Кинопоиск онлайн API")
@allure.title("Поиск филма по названию")
def test_poisk():
    fil = api.search_film_namen('Реквием по мечте')

    with allure.step("Сверяем статус результата"):
        assert fil.status_code == 200
    with allure.step("Сравниваем название фильма с введённым в поиск"):
        assert fil.json()["docs"][0]["name"] == "Реквием по мечте"


@allure.suite("Кинопоиск API")
@allure.feature("Позитивные проверки")
@allure.epic("Кинопоиск онлайн API")
@allure.title("Универсальный поиск фильмов")
def test_universal():
    with allure.step("Поиск по жанру"):
        univ = api.universal_search_film('ужасы')

    with allure.step("Сверяем статус результата"):
        assert univ.status_code == 200
    with allure.step("Сверяем жанр фильма с заданным"):
        assert univ.json()["docs"][3]["genres"][0]["name"] == "ужасы"


@allure.suite("Кинопоиск API")
@allure.epic("Кинопоиск онлайн API")
@allure.feature("Позитивные проверки")
@allure.title("Список жанров")
def test_list():
    lis = api.list_genre()

    with allure.step("Сверяем статус результата"):
        assert lis.status_code == 200


@allure.suite("Кинопоиск API")
@allure.epic("Кинопоиск онлайн API")
@allure.feature("Негативные проверки")
@allure.title("Поиск фильма по id")
def test_film_id():
    with allure.step("Вводим id, только вместо цифр буквы"):
        id_fil = api.search_film_id('боб')

    with allure.step("Сверяем статус результата"):
        assert id_fil.status_code == 400


@allure.suite("Кинопоиск API")
@allure.epic("Кинопоиск онлайн API")
@allure.feature("Негативные проверки")
@allure.title("Поиск фильма по рейтингу")
def test_rating():
    with allure.step("Вводим рейтинг, выходящий из-за границы предела"):
        ra = api.search_film_rating("12")

    with allure.step("Сверяем статус результата"):
        assert ra.status_code == 400
