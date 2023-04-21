from bs4 import BeautifulSoup

# (1) 로컬 파일 읽기
file = open('d:/hello-git/workspace/chap09/data/html02.html', mode = 'r', encoding = 'utf-8')
source = file.read()

# (2) html 파싱
html = BeautifulSoup(source, 'html.parser')
print(html)

# (3) a 태그 찾기
links = html.find_all('a')
print('links size =', len(links))

# (4) a태그에서 속성 찾기
for link in links:
    try :
        print(link.attrs['href'])
        print(link.attrs['target'])
    except Exception as e :
        print('예외 발생 :', e)

# (5) 정규표현식으로 속성 찾기
import re
print('패턴 객체 이용 속성 찾기')
patt = re.compile('http://')
links = html.find_all(href= patt)
print(links)
