import pandas as pd

d_path = 'D:/hello-git/workspace/chap08/data/emp.csv'
print(type(d_path))

employee = pd.read_csv(d_path, encoding = 'utf-8')

print(employee.head())
print(employee.info())

name = employee.Name
pay  = employee.Pay

from statistics import mean

print('관측치 길이 :', len(name))

print('전체 평균 급여 :', (mean(pay),1))
print('최저급여 :', min(pay), )

