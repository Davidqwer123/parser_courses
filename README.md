# 📊 NBU Currency Rates Parser

Цей Python-скрипт отримує актуальні курси валют з офіційного API Національного банку України (НБУ) та зберігає їх у CSV-файл `nbu_rates_correct.csv`.

## 🔧 Що робить скрипт:
- Надсилає запит до API НБУ: https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json
- Отримує курси валют на поточну дату
- Зберігає результати у файл `nbu_rates_correct.csv` з такими полями:
  - `currency` — назва валюти (наприклад, "Долар США")
  - `code` — буквений код валюти (наприклад, "USD")
  - `units` — кількість одиниць (фіксовано 1)
  - `rate` — курс валюти
  - `date` — дата оновлення курсу

## 🧪 Приклад використання:

```bash
python parser.py
```

Після виконання буде створено файл `nbu_rates_correct.csv` з усіма валютами, відсортованими за кодом.

## 📁 Вміст CSV-файлу:

```
currency,code,units,rate,date
Австралійський долар,AUD,1,25.34,2025-06-24
...
```

## 📦 Залежності

- Python 3.x
- Бібліотека `requests`

### Встановлення залежностей:

```bash
pip install requests
```

## 🧑‍💻 Автор

- ✨ Створено з любов’ю до даних
- 📅 Актуально на момент запуску: 2025-06-24

---

🔗 API НБУ: [https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json](https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json)
