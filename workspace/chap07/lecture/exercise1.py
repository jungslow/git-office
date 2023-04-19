from re import findall, split, match, compile

email1 = """hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""

for e in email1.split(sep='\n') :
    result = findall('^[a-z]\\w{3,}@[a-z]\\w{2,}.[a-z]\\w{,2}', e)

    # 패턴과 일치하는 email1
    if result :
        str_result = result[0]
        print('findall : ', str_result)
    print('='*30)

for e in email1.split(sep='\n'):
    # match
    result2 = match('^[a-z]\\w{3,}@[a-z]\\w{2,}.[a-z]\\w{,2}', e)

    if result2 :
        print('match : ', e)

