import urllib.request as ur
#import os, re, usecsv
from bs4 import BeautifulSoup as bs

TAG = 'tag/love/page/'
PAGE = 1
URL = f'https://quotes.toscrape.com/{TAG}{PAGE}/'

def get_quotes():
  soup = bs(ur.urlopen(URL).read(), 'html.parser')
  quotes_list = soup.find_all('span', {'class':'text'})
  return quotes_list

