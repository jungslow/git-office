from re import sub

st3 = 'test^홍길동 abc 대한*민국 123$tbc'

test1 = sub('[\^*$]+', '', st3)
print(test1)

test2 = sub('[0-9]', '', test1)
print(test2)


