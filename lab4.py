import math
import pylab
from matplotlib import mlab
import matplotlib.pyplot as plt
import numpy as np

n = float(input("Введите период сглаживания: "))  # период сглаживания
y = []   # значение y
a = 25  #t
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
for i in range(a):
    new_element = int(input("Введите y(a): "))  # xi
    y.append(new_element)

x = []
def f(y):

 for i in range((y + 1) or (y - 1)):
     new_element = (y[i-1] + y[i] + y[i+1])/n  # zi
     x.append(new_element)

X = np.array(x)
Y = np.array(y)
T = np.array(t)

for i in range(a):
    line_10, line_20 = plt.plot(T, Y, T, X)

plt.title(u'График SMA')

plt.xlabel(u't')
plt.ylabel(u'Значения')

plt.legend( (line_10, line_20), (u'График значений до обработки', u'График значений после обработки'))

plt.grid()

plt.savefig('spirit.png', format = 'png')
