import requests
import urllib.request as ur
#import os, re, usecsv
from bs4 import BeautifulSoup as bs

URL = 'https://quotes.toscrape.com/'

def get_quotes():
  soup = bs(ur.urlopen(URL).read(), 'html.parser')
  quotes_list = soup.find_all('div', {'class':'quote'})
  return quotes_list

