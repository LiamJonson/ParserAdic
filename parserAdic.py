import requests
from bs4 import BeautifulSoup
import csv



data_gl = []


def get_html(url):
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        r = session.get(url)
    return r.text

def write_csv(data): #recording csv
    with open('adic.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';')
        for line in data:
            writer.writerow(line)

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.findAll('div', class_='hockeycard terrex')
    for ad in ads:
        #print(ad)
        title = ad.find('span', {'class': 'title'}).text
        print(title)
        url = ad.find('div',class_="product-info-inner-content clearfix with-badges").find('a').get('href')
        print(url)
        price = ad.find('span',{'class':'salesprice discount-price'}).text.split()
        print(price)
        data = [ title,
                price,
               'https://www.adidas.ru'+url]
        data_gl.append(data)
        write_csv(data_gl)



def main():
    base_url = 'https://www.adidas.ru/muzhchiny-obuv-terrex-outlet?prefn1=sizeSearchValue&prefv1=42'
    html = get_html(base_url)
    get_page_data(html)

if __name__ == '__main__':
    main()