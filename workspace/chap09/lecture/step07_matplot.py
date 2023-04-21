import matplotlib.pyplot as plt
import random

import matplotlib

plt.rcParams['axes.unicode_minus'] = False

print(random.randint(a=1, b=5))
print(random.random())
print(random.normalvariate(mu=0, sigma=1))

data = range(10)
plt.plot(data)
plt.plot(data, 'r+')
plt.show()

data2 = [random.random() for i in range(10)]
plt.plot(data, data2)
plt.plot(data, data2, 'ro')
plt.show()


