#-*- coding: utf-8 -*-
import numpy as np

###### 유니버셜 함수
x = np.arange(10)
y = np.arange(10)*10
z = np.random.randn(7) * 5
print("\nx: ", x)
print("\ny: ", y)
print("\nz: ", z)
print("\nsqrt :", np.sqrt(x))
print("\nmaximum :", np.maximum(x, y))
print("\nmodf of z :", np.modf(z))
print("\nabs z :", np.abs(z))
print("\ncosine z :", np.cos(z))
print("\npower (y, x) :", np.power(y, x))
print("\nequal (x, y) :", np.equal(x, y))


