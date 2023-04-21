from bs4 import BeautifulSoup

#  (1)
file = open('d:/hello-git/workspace/chap09/data/html01.html', mode = 'r', encoding = 'utf-8')
text = file.read()

# (2) html 파싱
html = BeautifulSoup(text, 'html.parser')

# (3-1) 태그 내용 가져오기
h1 = html.html.body.h1
print('h1 :', h1.string)

# (3-2) 태그 내용 가져오기
h2 = html.find('h2')
print('h2 :', h2.string)

# (3-3) 태그 내용 가져오기
lis = html.find_all('li')
print(lis)
print('*'*55)

# (4) li 태그 내용
for li in lis :
    print(li.string)


