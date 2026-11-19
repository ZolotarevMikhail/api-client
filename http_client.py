"""HTTP-клиент: ключ из .env и GET-запросы с Authorization."""
import os

import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_env(path):
    """Читает .env (строки KEY=VALUE, без #) и задаёт переменные окружения."""
    if not os.path.exists(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())


load_env(os.path.join(BASE_DIR, ".env"))
API_KEY = os.getenv("RESTCOUNTRIES_KEY", "")


def get(url, params=None, timeout=10):
    """GET-запрос: статус и текст печатает, при не-200 возвращает None."""
    headers = {}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    response = requests.get(
        url, params=params, timeout=timeout, headers=headers
    )
    if response.status_code != 200:
        print("Ошибка:", response.status_code)
        return None
    print(response.status_code)
    print(response.text)
    return response
