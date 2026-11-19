# API-клиент в терминале

Консольная программа на Python: запрашивает информацию о странах через restcountries и случайные фото собак через dog.ceo.

## Как запустить

1. Получи бесплатный ключ на restcountries.com (кнопка Get an API key).
2. Создай файл `.env` рядом с main.py и вставь ключ:

```
RESTCOUNTRIES_KEY=твой_ключ
```

3. Запусти:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
