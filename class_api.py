import requests
api_url = 'https://api.kinopoisk.dev'

hed = {
        'accept': 'application/json',
        'X-API-KEY': 'DA5WC8Z-X4B4TSK-NSC813H-8DJQJC3'
    }

class ApiKinopoisk():
    def search_film_namen():
        nam = requests.get(api_url + '/v1.4/movie/search?page=1&limit=10&query=Реквием по мечте', headers=hed)

        return nam

    def universal_search_film():
        uni = requests.get(api_url + '/v1.4/movie?page=1&limit=10&rating.kp=6.3-10&genres.name=ужасы', headers=hed)

        return uni

    def list_genre():
        gen = requests.api.get(api_url + '/v1/movie/possible-values-by-field?field=genres.name', headers=hed)

        return gen

    def search_film_id():
        idy = requests.get(api_url + '/v1.4/movie?id=боб', headers=hed)

        return idy

    def search_film_rating():
        rat = requests.get(api_url + '/v1.4/movie?page=1&limit=10&rating.kp=12', headers=hed)

        return rat
