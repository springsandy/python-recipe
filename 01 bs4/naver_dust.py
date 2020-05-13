from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text)

SOUP = bs(html.text, 'html.parser')
#pprint(SOUP)

detal = SOUP.find('div', {'class' : 'detail_box'})
pprint(detal)