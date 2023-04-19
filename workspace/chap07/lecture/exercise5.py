from re import findall, sub

texts = ['AFAB54747, asabag?', 'abTTa $$;a12:2424.', 'uysfA,a124&***$?']

# 소문자 변경
string = 'ABCd'
print(string.lower())
print(string.upper())

# list 내포
texts_re = [t.lower() for t in texts]
print('texts_re :', texts_re)

# 숫자 제거
texts_re2 = [''.join(findall("[^0-9]", text)) for text in texts_re]
print('texts_re2 :', texts_re2)

# 문장부호 제거
punc_str = '[,..!?:;]'
texts_re3 = [sub(punc_str, '', text) for text in texts_re2]
print('texts_re3 :', texts_re3)

# 특수문자 제거
spec_str = '[@#$%^&*()]'
texts_re4 = [sub(spec_str, '', text) for text in texts_re3]
print('texts_re4 :', texts_re4)

# 공백 제거
texts_re5 = [''.join(text.split()) for text in texts_re4]
print('texts_re5 :', texts_re5)

