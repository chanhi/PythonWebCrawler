this is my first web crawler making by python
### NOMARD CODER
### DO it! 파이썬 생활 프로그래밍

BeautifulSoup

    find_all()

리스트로 반환

    find()

문자열?로 반환

    find('...').find('...")...

자식의 자식의 자식의... 찾을 수 있음

    find('...')[...]

찾은 내용중 []안에 있는 element를 출력

(TAG,{CLASS:NAME})[UNDER_TAG]

    BeautifulSoup(HTML, "HTML.parse")

request
requests.get(URL)

urllib

###indeed.py

'extract_indeed_pages()'
class가 pagination이면서 제일 먼저 있는 div

    find("div", {"class":"pagination"})

찾은 div 안에서 a태그 찾기

    pagination.find_all('a')

max_page에 1...마지막 페이지 까지 저장

