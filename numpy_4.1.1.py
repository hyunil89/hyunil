########### 4.1 NumPy ndarray

import numpy as np

# 2 by 3 random array
data = np.random.randn(2, 3)
print("1: ", data)

data = data * 10
print("2: ", data)

print("data.shape: ", data.shape)
print("data.dtype: ", data.dtype)
##############################


########### 4.1.1 Generate ndarray

data1 = [6, 7.5, 0]
arr1 = np.array(data1)
print("arr1: ", arr1)
print("arr1.shape: ", arr1.shape)
print("arr1.dtype: ", arr1.dtype)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print("arr2: ", arr2)
print("arr2.ndim: ", arr2.ndim)
print("arr2.shape: ", arr2.shape)
print("arr2.dtype: ", arr2.dtype)

## zeros, empty, range
print("zeros: ", np.zeros(10))
print("empty: ", np.empty((2, 3, 2)))#Array of uninitialized (arbitrary) data
print("arange: ", np.arange(15))

##배열생성함수##
#asarray : No copy is performed if the input is already an ndarray.
#          If input is a subclass of ndarray, a base class ndarray is returned
copy_asarray = np.array(arr1)
print("asarray: ", copy_asarray)
print(np.asarray(arr1) is arr1)  #arr1이 이미 nparray이기 때문에 True 반환

arr_test=np.array(data1)
print(np.asarray(data1) is data1)  #data1은 nparray가 아니기 때문에 False 반환

#ones_like : return an array of ones with shape and type of input
#ones : return a new array setting values to one
arr_ones=np.ones(10)
print("ones(10): ", arr_ones)
print(arr_ones.dtype)
print("ones_like(10): ", np.ones_like(10))
float_arr = np.random.randn(10)
#float_arr = [3, 5, 6]
print(float_arr.dtype)
#print("ones(arr) : ", np.ones(float_arr))    #ValueError : negative dimensions are not allowed
print("ones_like(arr): ", np.ones_like(float_arr))

#eye, identity : 단위행렬
print("eye:\n ", np.eye(10))
print("identity:\n ", np.identity(10))

###############

##############################


