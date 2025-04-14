from class_api import ApiKinopoisk

api = ApiKinopoisk

# Позитивные проверки
def test_poisk():
    fil = api.search_film_namen().status_code

    assert fil == 200

def test_universal():
    univ = api.universal_search_film().status_code

    assert univ == 200

def test_list():
    lis = api.list_genre().status_code

    assert lis == 200

# Негативные проверки
def test_film_id():
    id_fil = api.search_film_id().status_code

    assert id_fil == 400

def test_rating():
    ra = api.search_film_rating().status_code

    assert ra == 400
