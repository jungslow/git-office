import os
import re

d_path = 'D:/hello-git/workspace/chap08/data/ftest.txt'
file = open(d_path, mode = 'r')
print(type(d_path))

lines = file.readlines()
print('문장 내용', lines)
print('문장 수 : ', len(lines))

docs = []
words = []

# '\n' 제거
for line in lines :
    docs.append(line.strip())
    for word in line.split() :
        words.append(word)

print(docs)
print('문단 길이 :', len(docs))

print(words)
print('단어 수 :', len(words))








