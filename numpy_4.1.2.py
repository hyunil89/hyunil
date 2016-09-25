#-*- coding: utf-8 -*-
import numpy as np

########### 4.1.2 ndarray의 자료형

arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)

print("arr1 type:\n", arr1.dtype)
print("arr2 type:\n", arr2.dtype)

###
print("astype : 부동소수점 -> 정수형일 시 소수점 아랫자리 버려짐")
arr = np.array([3.54, -1.23, 0.5])
int_arr = arr.astype(np.int32)
print("arr :\n", arr)
print("arr type:\n", arr.dtype)
print("int_arr :\n", int_arr)
print("int_arr type:\n", int_arr.dtype)

str_arr = arr.astype(np.string_)
print("str_arr :\n", str_arr)
print("str_arr type:\n", str_arr.dtype)

###
print("\n다른 ndarray의 타입 복사")
int_array = np.arange(10)
print("before int_array :\n", int_array)
calibers = np.array([.22, .270], dtype=np.float64)
int_array = int_array.astype(calibers.dtype)
print("int_array :\n", int_array)
print("int_array type:\n", int_array.dtype)
##############################
