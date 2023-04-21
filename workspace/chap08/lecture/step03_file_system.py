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

os.chdir('..')
print(os.getcwd())

os.path.abspath('lecture/step01_try_except.py')
print(os.path.abspath('lecture/step01_try_except.py'))

os.path.dirname('lecture/step01_try_except.py')
print(os.path.dirname('lecture/step01_try_except.py'))

os.path.exists('d:/hello-git/workspace/chap08')
print(os.path.exists('d:/hello-git/workspace/chap08'))

os.path.isfile('lecture/step01_try_except.py')
print(os.path.isfile('lecture/step01_try_except.py'))

os.path.isdir('lecture')
print(os.path.isdir('lecture'))

os.path.split('C://test/test1.txt')
print(os.path.split('C://test/test1.txt'))
print(os.path.join('C:\\test', 'test1.txt'))

print(os.path.getsize('lecture/step01_try_except.py'))




