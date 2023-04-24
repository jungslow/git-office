from bs4 import BeautifulSoup

file = file = open('d:/hello-git/workspace/chap09/data/login.html', mode = 'r', encoding ='utf-8')
source = file.read()

html = BeautifulSoup(source, 'html.parser')
print(html)

trs= html.find_all('tr')
print('tr 내용', trs)

print('\nth tag 내용')
for tr in trs :
    th = tr.find('th')
    print(th.string)



