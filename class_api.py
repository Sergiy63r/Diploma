import requests

api_key = {
        'X-API-KEY': 'DA5WC8Z-X4B4TSK-NSC813H-8DJQJC3'
    }


class ApiKinopoisk():
    def __init__(self, api_url):
        self.api_url = api_url

    def search_film_namen(self, title: str):
        """
           Поиск фильма по названию.
           Можно указывать часть названия, если не помните полное.
           Поиск будет произведён и вам откроется список фильмов
           в которых будет присутствовать часть введённого низания.
        """
        nam = requests.get(self.api_url + '/v1.4/movie/search?page=1&limit=10&query=' + title, headers=api_key)    # noqa: E501

        return nam

    def universal_search_film(self, title: str):
        """
           Поиск фильма по жанру.
             Жанры: аниме, биография, боевик, вестерн, военный,
           детектив, детский, для взрослых, документальный, драма,
           игра, история, комедия, концерт, короткометражка,
           мелодрама, музыка, мультфильм, мюзикл, новости,
           приключения, реальное ТВ, семейный, спорт, ток-шоу,
           триллер, ужасы, фантастика, фильм-нуар, фэнтези, церемония.
        """
        uni = requests.get(self.api_url + '/v1.4/movie?page=1&limit=10&rating.kp=6.3-10&genres.name=' + title, headers=api_key)    # noqa: E501

        return uni

    def list_genre(self):
        gen = requests.api.get(self.api_url + '/v1/movie/possible-values-by-field?field=genres.name', headers=api_key)    # noqa: E501

        return gen

    def search_film_id(self, title: int):
        """
           Поиск фильма по id.
           id не должен принимать буквы и символы.
        """
        idy = requests.get(self.api_url + '/v1.4/movie?id=' + title, headers=api_key)    # noqa: E501

        return idy

    def search_film_rating(self, title: int):
        """
           Поиск фильма по рейтингу.
           Диапазон рейтинга от 1 до 10.
        """
        rat = requests.get(self.api_url + '/v1.4/movie?page=1&limit=10&rating.kp=' + title, headers=api_key)    # noqa: E501

        return rat
