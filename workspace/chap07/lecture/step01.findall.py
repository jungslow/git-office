from re import findall

st1 = '1234 abc홍길동 ABC_555_6 이사도시'

print(findall('[0-9]', st1))
print(findall('[0-9]{3}', st1))
print(findall('[0-9]{3,}', st1))
print(findall('\\d{3,}', st1))

print(findall('[가-힣]{3,}', st1))
print(findall('[a-z]{3}', st1))
print(findall('[a-z|A-Z]{3}', st1))

st2 =  'test1abcABC 123mbc 45test'
print(findall('test', st2))
print(findall('.bc', st2))
print(findall('st$', st2))
print(findall('c.', st2))
print(findall('t.', st2))

st3 = 'test^홍길동 abc 대한*민국 123$tbc'
words = findall('\\w{3,}', st3)
print(words)

print(findall('[^^*$]+', st3))

