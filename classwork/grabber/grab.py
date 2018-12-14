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
    soup = BeautifulSoup(res.content)

    pricing = soup.find('div', class_='pricing-table')
    tables = pricing.find_all('table', class_='table')

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
            print(cur, buy, sell)


    # return [
    #     {
    #         'cur': cur,
    #         'buy': pk,
    #         'sell': pr
    #     },
    #     {
    #         'cur': cur_2,
    #         'buy': pk_2,
    #         'sell': pr_2
    #     }
    # ]

def get_kicb():
    print('kicb')

def get_cbk():
    print('cbk')

main()
