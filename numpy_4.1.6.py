#-*- coding: utf-8 -*-
import numpy as np

arr = np.empty((8, 4))

print(arr)
for i in range(8):
    arr[i] = i*100

print(arr)

print("\n4, 3, 0, 6의 순서대로 row 출력\n", arr[[4, 3, 0, 6]])
print("\n-1, -3, -5, -7의 순서대로 row 출력 ; 거꾸로 출력됨(-1=7, -3=5, -5=3, -7=1)\n", arr[[-1, -3, -5, -7]])

##### 다차원 색인 배열 넘기는 방법
print("------------------")
arr = np.arange(32).reshape((8, 4))
print(arr)

print("예상과 다르게 (1,0), (5,3), (7,1), (2,2)가 출력됨.")
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])

print("\n4 by 4, 즉 1, 5, 7, 2행을 0, 3, 1, 2의 순서대로 배열한 값을 출력하려면")
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
print("\n또는 np.ix_ 함수 사용")
print(arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
