import os

print(os.getcwd())

os.chdir('d:/hello-git/workspace/chap08/data/')
print(os.getcwd())

os.mkdir('test')
print(os.listdir('.'))

os.chdir('test')
print(os.getcwd())

os.makedirs('test2/test3')
print(os.listdir('.'))

os.chdir('test2')
print(os.listdir('.'))

os.rmdir('test3')
print(os.listdir('.'))

os.chdir('../..')
print(os.getcwd())

os.removedirs('test/test2')


