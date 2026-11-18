import requests


def get(url, params=None, timeout=10):
    response = requests.get(url, params=params, timeout=timeout, headers={"Authorization": "Bearer rc_live_demo"})
    if response.status_code != 200:
        print("Ошибка:", response.status_code)
        return None
    print(response.status_code)
    print(response.text)
    return response
