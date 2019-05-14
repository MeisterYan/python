import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/cinema/later/kunming/'
f = requests.get(url)
soup = BeautifulSoup(f.content, 'lxml')
#print(soup)
for a in soup.find_all('div', class_='intro'):
    for name in a.find_all('a', class_=''):
#        print(name)
        a = list(name)
        print(a[0])