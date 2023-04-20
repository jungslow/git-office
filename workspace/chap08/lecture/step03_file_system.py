import os

print(os.getcwd())

os.chdir('../data')
print(os.getcwd())

os.mkdir('test001')
print(os.listdir('.'))

os.mkdir('test002/test003')
print(os.listdir('.'))

