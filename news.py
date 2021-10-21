import requests
from bs4 import BeautifulSoup as bs

URL = "https://news.daum.net/"
result = requests.get(URL)
soup = bs(result.text, "html.parser")



def find_hdline():
  link_list = []
  for i in soup.find_all('div', {"class":"item_issue"}):
    link_list.append((i.find_all('a')[0].get('href')))
  
  soup_headline_news = bs(requests.get(link_list[0]).text, "html.parser")
  for i in soup_headline_news.find_all('div', {'class':"article_view"}):
    print(i.find_all('p'))



def test():
  print(soup.find_all('div', {'class':"feature_home"}))

