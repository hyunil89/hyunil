#-*- coding: utf-8 -*-
import numpy as np

########### 4.1.4 색인과 슬라이싱 기초
print("\n1차원 배열 ")

arr = np.arange(10)
print("arr:\n", arr)
print("arr[5]:\n", arr[5])
print("arr[5:8]:\n", arr[5:8])

print("리스트와의 차이점 : 데이터 복사가 이루어지지 않음.")
arr[5:8] = 12
print("arr:\n", arr)

arr_slice = arr[5:8]
arr_slice[1] = 12345
print("arr:\n", arr)   #원본데이터의 값이 변하는 것을 알 수 있다.

arr_slice[:] = 64
print("arr:\n", arr)

print("데이터를 복사하려면 copy 사용")
arr_slice = arr[5:8].copy()
arr_slice[1] = 3333
print("arr:\n", arr)   #원본데이터의 값이 변하지 않음
print("arr_slice:\n", arr_slice)   #데이터 일부분 복사 가능

######
print("\n2차원 배열 ")

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("arr2d:\n", arr2d)

print("\n개별 요소 접근")
print("arr2d[0][2]: ", arr2d[0][2])
print("arr2d[0][2]: ", arr2d[0, 2])

######인
print("\n3차원 배열 ")
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("arr3d:\n", arr3d)
print("arr3d[0]:\n", arr3d[0])

arr3d[0] = 42
print("\n변형된 arr3d:\n", arr3d)
print("\narr3d[1, 0]:\n", arr3d[1, 0])


###### 슬라이스 색인
print("\n1차원 슬라이스 ")
print("\narr :", arr)
print("arr[1:6] :", arr[1:6])

print("\n2차원 슬라이스 ")
print("\narr2d :\n", arr2d)
print("arr2d[0:2]\n :", arr2d[:2])

print("\n2차원에서 여러개 슬라이스 ")
print("\n[:a, b:] - a행까지 슬라이스 후 내부에서 b열부터 슬라이스")
print("arr2d :\n", arr2d)
print("arr2d[:2, 1:]\n :", arr2d[:2, 1:])

print("\n[a, :b]- a번째 행에서 b열까지 슬라이스")
print("arr2d :\n", arr2d)
print("arr2d[2, :1]\n :", arr2d[2, :1])

print("\n[:, :b] - 모든 행에서 b열까지 슬라이스")
print("arr2d :\n", arr2d)
print("arr2d[:, :1]\n :", arr2d[:, :1])

print("\n[a:, :b] - a행부터 b열까지 슬라이스")
print("arr2d :\n", arr2d)
print("arr2d[1:, :2]\n :", arr2d[1:, :2])
