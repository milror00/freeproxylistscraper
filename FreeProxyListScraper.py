# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests



class FreeProxyListScraper():

    def __init__(self):
        self.url = 'https://free-proxy-list.net/'

    def get_url(self):
        try:
            request = requests.get(url=self.url)
            request.encoding = 'utf-8'
            html = request.text
            self.page_bf = BeautifulSoup(html, 'lxml')
        except Exception as e:
            print(e)
            exit(1)

    def get_all_table_rows(self):
        # all table rows
        tables = self.page_bf.find('table',id='proxylisttable')
        print(tables)
        rows = tables.findChildren('tr')
        return rows

    def get_all_proxies(self):
        self.get_url()
        rows = self.get_all_table_rows()
        results = []
        for row in rows:
            cells = row.findChildren('td')
            proxies = {}
            for cell in cells:
                proxies['ipaddress'] = cells[0].string
                proxies['port'] = cells[1].string
                proxies['countrycode'] = cells[2].string
                proxies['country'] = cells[3].string
                proxies['anonymity'] = cells[4].string
                if cells[5].attrs['class'] == 'hx':
                     proxies['https'] = cells[5].string
                else:
                    proxies['https'] = cells[6].string
                results.append(proxies)
                break
        return results

if __name__ == '__main__':
    proxies = FreeProxyListScraper()
    results = proxies.get_all_proxies()
    #headers
    print('|{0: <10}|{1: <20}|{2: <15}|{3: <15}|{4: <15}|'.format(
        'IP Address',
        'Port',
        'Country code',
        'Anonymity',
        'HTTPS'))
    print('|----------|-------------------|---------------|---------------|---------------|')
    #data
    for currency in results:
        print('|{0: <10}|{1: <20}|{2: <15}|{3: <15}|{4: <15}|'.format(
            currency['ipaddress'],
            currency['port'],
            currency['countrycode'],
            currency['anonymity'],
            currency['https'],
        ))