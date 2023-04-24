from bs4 import BeautifulSoup

file = file = open('d:/hello-git/workspace/chap09/data/login.html', mode = 'r', encoding ='utf-8')
source = file.read()

html = BeautifulSoup(source, 'html.parser')
print(html)

dev = html.select_one('div#login_wrap')
print("login_wrap table", dev)

table = dev.select_one('div#login_wrap > form > table')
print("select table", table)
print()

print(" 3. table > tr > th/td 태그 내용 출력")
trs = html.find_all('tr')
print(trs)

print(" \nth 내용 출력")
for tr in trs :
    th = tr.find('th')
    print(th.string)

# 요소안의 요소 추출
print(" \ntd input 태그 내용")
for tr in trs :
    tds = tr.find('td')
    inp = tds.find('input')
    print(inp)

inputs = html.find_all('input')
print(inputs)

print(" \ninput 태그의 value 속성 값")
for inp in inputs :
    if 'value' in inp.attrs :
        value = inp.attrs['value']
        print(value)





