import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'

r = requests.get(url).text

soup = BeautifulSoup(r, 'lxml')

for article in soup.find_all('article'):
    # print(article.prettify())

    headline = article.h2.text

    print(headline + '\n')
