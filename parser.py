import requests
import csv
from datetime import datetime

def parse_nbu_rates_api():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    resp = requests.get(url)
    resp.raise_for_status()
    rates = resp.json()

    data = []
    today = datetime.now().strftime("%Y-%m-%d")
    for item in rates:
        data.append({
            'currency': item.get('txt'),
            'code': item.get('cc'),
            'units': 1,  # API дає курс для 1 одиниці
            'rate': float(item.get('rate')),
            'date': today
        })

    data.sort(key=lambda x: x['code'])

    with open('nbu_rates_correct.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['currency','code','units','rate','date'])
        writer.writeheader()
        writer.writerows(data)

    print(f"Збережено {len(data)} курсів у nbu_rates_correct.csv")

if __name__ == "__main__":
    parse_nbu_rates_api()
