import requests
from bs4 import BeautifulSoup

print('Grabber')


def main():
    print('main')
    dem = get_demir()
    print('dem', dem)


def get_demir():
    print('demir')

    res = requests.get('http://www.demirbank.kg/ru')
    soup = BeautifulSoup(res.content, 'html.parser')

    pricing = soup.find('div', class_='pricing-table')
    tables = pricing.find_all('table', class_='table')

    ret = []
    for table in tables:
        trs = table.find_all('tr')
        for tr in trs:
            th = tr.find('th')
            cur = None
            if th:
                cur = th.get_text()
            tds = [td.get_text() for td in tr.find_all('td') if td.get_text()]
            buy, sell = None, None
            if tds:
                buy, sell = tds

            if all([cur, buy, sell]):
                ret.append({
                    'cur': cur,
                    'buy': float(buy),
                    'sell': float(sell)
                })
    return ret

def get_kicb():
    ret = [{'cur': 'EUR', 'buy': 78.5, 'sell': 79.8}, {'cur': 'USD', 'buy': 69.7, 'sell': 69.9},
           {'cur': 'RUB', 'buy': 1.04, 'sell': 1.065}, {'cur': 'TRY', 'buy': 12.05, 'sell': 13.17},
           {'cur': 'KZT', 'buy': 0.181, 'sell': 0.191}, {'cur': 'EUR', 'buy': 77.97, 'sell': 79.58},
           {'cur': 'USD', 'buy': 69.65, 'sell': 69.9}, {'cur': 'RUB', 'buy': 1.028, 'sell': 1.074},
           {'cur': 'TRY', 'buy': 12.3, 'sell': 13.66}, {'cur': 'KZT', 'buy': 0.184, 'sell': 0.1924}]
    return ret

def get_cbk():
    ret = [{'cur': 'EUR', 'buy': 78.5, 'sell': 79.8}, {'cur': 'USD', 'buy': 69.7, 'sell': 69.9},
           {'cur': 'RUB', 'buy': 1.04, 'sell': 1.065}, {'cur': 'TRY', 'buy': 12.05, 'sell': 13.17},
           {'cur': 'KZT', 'buy': 0.181, 'sell': 0.191}, {'cur': 'EUR', 'buy': 77.97, 'sell': 79.58},
           {'cur': 'USD', 'buy': 69.65, 'sell': 69.9}, {'cur': 'RUB', 'buy': 1.028, 'sell': 1.074},
           {'cur': 'TRY', 'buy': 12.3, 'sell': 13.66}, {'cur': 'KZT', 'buy': 0.184, 'sell': 0.1924}]
    return ret


main()
