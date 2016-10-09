#-*- coding: utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

from numpy import nan as NA

df = DataFrame(np.random.randn(7, 3))

df.ix[:4, 1] = NA; df.ix[:2, 2] = NA

# NA를 채우기
df.fillna(0)

# 사전 값을 넘겨서 각 칼럼마다 다른 값을 채울수도 있음
df.fillna({1: 0.5, 3: -1})

# fillna는 새로운 객체를 반환하지만 기존 객체도 변경 가능
df.fillna(0, inplace=True)
df

# ffill
df = DataFrame(np.random.rnadn(6, 3))
df.ix[2:, 1] = NA; df.ix[4:, 2] = NA
df

df.fillna(method = 'ffill')
df.fillna(method = 'ffill', limit = 2)

# fillna를 이용해 Series의 평균이나 중간값 등의 연산 전달 가능
data = Series([1., NA, 3.5, NA, 7])
data.fillna(data.mean())
