from re import findall, sub

texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 15000GRAM 정력 최고',
         '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

def clean_text(text):
    texts_re1 = text.lower()                        # 소문자 제거
    texts_re2 = sub('[0-9]', '', texts_re1)         # 숫자 제거
    texts_re3 = sub('[,.!?:;]', '', texts_re2)      # 문장부호 제거
    texts_re4 = sub('[@#$%^&*()]', '', texts_re3)   # 특수문자 제거
    texts_re5 = sub('[a-z]', '', texts_re4)         # 영문자 제거
    texts_re6 = ' '.join(texts_re5.split())         # White space 제거
    return texts_re6

# clean_text() 함수 호출 및 출력
texts_result = [clean_text(text) for text in texts]
print(texts_result)


