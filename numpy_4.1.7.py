#-*- coding: utf-8 -*-
import numpy as np

##### 배열 전치와 축 바꾸기

arr = np.arange(15).reshape((3, 5))

print(arr)

print("행렬 arr의 transpose :\n", arr.T)

print("np.dot함수 사용 - 행렬 arr의 내적 :\n", np.dot(arr.T, arr))

## 3차원 행렬
print("\n3차원 행렬 transpose")

arr = np.arange(16).reshape((2, 2, 4))
print("\noriginal :\n", arr)

print("\narr.transpose((1, 0, 2)) :\n", arr.transpose((1, 0, 2)))
print("\narr.transpose((1, 2, 0)) :\n", arr.transpose((1, 2, 0)))

print("\nswapaxes(0, 1):\n", arr.swapaxes(0, 1))

