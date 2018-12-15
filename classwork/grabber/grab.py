import requests
from bs4 import BeautifulSoup

print('Grabber')


def main():
    print('main')
    all_data = {}
    all_list = []

    for item in get_demir():
        all_list.append(item)

    for item in get_kicb():
        all_list.append(item)

    for item in get_cbk():
        all_list.append(item)

    for _list in all_list:
        currency = _list['cur']
        if currency not in all_data:
            all_data[currency] = {
                'buy': [],
                'sell': [],
            }

        all_data[currency]['buy'].append(_list['buy'])
        all_data[currency]['sell'].append(_list['sell'])

    for currency, _data in all_data.items():
        print(currency)
        print(sum(_data['buy']) / len(_data['buy']))
        print(sum(_data['sell']) / len(_data['buy']))
        print('----------------------')

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
    ret = [
        {'cur': 'EUR', 'buy': 79.5, 'sell': 79.6},
        {'cur': 'USD', 'buy': 69.1, 'sell': 69.2},
        {'cur': 'RUB', 'buy': 1, 'sell': 1.165},
        {'cur': 'TRY', 'buy': 12.056, 'sell': 14.17},
        {'cur': 'KZT', 'buy': 0.281, 'sell': 0.161},
    ]
    return ret


def get_cbk():
    ret = [
        {'cur': 'EUR', 'buy': 76.5, 'sell': 79.83},
        {'cur': 'USD', 'buy': 66.7, 'sell': 69.94},
        {'cur': 'RUB', 'buy': 1.0411, 'sell': 1.0565},
        {'cur': 'TRY', 'buy': 12.051, 'sell': 13.176},
        {'cur': 'KZT', 'buy': 0.1812, 'sell': 0.1917},
    ]
    return ret


main()
