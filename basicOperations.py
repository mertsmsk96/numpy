# -*- coding: utf-8 -*-

import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)

c = a-b
d = b**3
e = 10 * np.sin(a)
print(e<7)
print(a*b) # elementwise product
print(a@b) #matris çarpımı
print(a.dot(b)) #matris çarpımı

f = np.ones((2,4))
g = np.zeros((2,4))
h = np.random.random((2,4))
i = np.sum(b)
j = np.min(b)
k = np.max(h)
print(b.sum())
l = np.sqrt(b)









