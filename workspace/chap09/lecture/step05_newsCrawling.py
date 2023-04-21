# (1) 모듈 import
import urllib.request as req
from bs4 import BeautifulSoup

# news 제공 포털 사이트
url = "http://media.daum.net"

# (1) url 요청
res = req.urlopen(url)
source = res.read()

# (2) source 디코딩
source = source.decode('utf-8')
print(type(source))

# (3) html 파싱
html = BeautifulSoup(source, 'html.parser')
print(type(html))

# (4) tab[속성=값] 요소 추출
atags = html.select('a[class=link_txt]')
print('a tag 수 =', len(atags), ', a tag type =', type(atags))

# (5) a 태그 내용 수집
crawling_data = []
cnt = 0
for atag in atags :
    cnt += 1
    atagStr = str(atag.string)
    crawling_data.append(atagStr.strip())

# 수집한 자료 확인
print('수집한 자료 확인')
print(crawling_data)

# (6) pickle save/load
import pickle # object ==> file(binary) ==> load(object)

# save : binary file save
file = open('d:/hello-git/workspace/chap09/data/data.pickle', mode = 'wb')
pickle.dump(crawling_data, file)

# load : binary file load
file = open('d:/hello-git/workspace/chap09/data/data.pickle', mode = 'rb')
crawling_data = pickle.load(file)
print('pickle load')
print(crawling_data)



