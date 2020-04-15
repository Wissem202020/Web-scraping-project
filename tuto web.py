import  requests
from bs4 import BeautifulSoup


url ='http://example.webscraping.com/'

res = requests.get(url)
if (res.ok):
    links = []
    soup = BeautifulSoup(res.text, 'lxml')
    tds = soup.findAll('td')
    for td in tds:
        a = td.find('a'
        link = a['href']
        links.append('http://example.webscraping.com + link'))
    print(str(tds) + \n\n) for d in tds )

    print('hhhhhhhhhhh')
