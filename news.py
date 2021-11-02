import requests
from bs4 import BeautifulSoup as bs

URL = "https://news.daum.net/"
result = requests.get(URL)
soup = bs(result.text, "html.parser")



def find_hdline():
  link_list = [] #헤드라인 뉴스의 URL
  #헤드라인 뉴스를 찾음
  for i in soup.find_all('div', {"class":"item_issue"}):
    print(i.text, '\n') #기사제목 출력
    link_list.append((i.find_all('a')[0].get('href')))
    soup_headline_news = bs(requests.get(link_list[0]).text, "html.parser")
    text_headline_news = soup_headline_news.find_all('p')
    for i in text_headline_news[:-3]:
      print(i.text) #찾은 뉴스의 기사를 출력

  return link_list
  


def test():
  for i in soup.find_all('div', {'class':"cont_thumb"}):
    print(i.text)

