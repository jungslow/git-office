from re import findall, sub

texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 15000GRAM 정력 최고',
         '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']


texts_re1 = [text.lower() for text in texts]
print('texts_re1 = ', texts_re1)

texts_re2 = [sub('[0-9]', '', text) for text in texts_re1]
print('texts_re2 = ', texts_re2)

texts_re3 = [sub('[,.!?:;]', '', text) for text in texts_re2]
print('texts_re3 = ', texts_re3)

texts_re4 = [sub('[@#$%^&*()]', '', text) for text in texts_re3]
print('texts_re4 = ', texts_re4)

texts_re5= [''.join(findall('[^a-z]', text)) for text in texts_re4]
print('texts_re5 = ', texts_re5)

texts_re6= [' '.join(text.split()) for text in texts_re5]
print('texts_re6 = ', texts_re6)







