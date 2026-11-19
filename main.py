"""Консольный клиент: GET по URL, данные по стране, случайная собака."""
from http_client import get


def make_get_request(url):
    """GET-запрос по любому URL: печатает статус и тело ответа."""
    response = get(url)
    print(response.status_code)
    print(response.text)
    return response


def make_get_country_request(country):
    """Данные по стране через Rest Countries v5: название, столица, регион."""
    url = f"https://api.restcountries.com/countries/v5/names.common/{country}"
    response = make_get_request(url)
    data = response.json()["data"]["objects"][0]
    print("Официальное название:", data["names"]["official"])
    print("Столица:", data["capitals"][0]["name"])
    print("Регион:", data["region"])


def make_get_dog_request():
    """Случайная фотография собаки из dog.ceo."""
    response = get("https://dog.ceo/api/breeds/image/random")
    picture = response.json()["message"]
    print("Ссылка на собаку:", picture)


while True:
    choice = input(
        "Выбери: 1 — GET по URL, 2 — Страна, "
        "3 — Случайная собака, 0 — Выход: ")
    if choice == "1":
        url = input("Введи URL: ")
        make_get_request(url)
    elif choice == "2":
        country = input("Введите страну: ")
        make_get_country_request(country)
    elif choice == "3":
        make_get_dog_request()
    elif choice == "0":
        break
