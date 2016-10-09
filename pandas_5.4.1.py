#-*- coding: utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# dropna : 실제 데이터가 들어있는 색인 값과 데이터를 Series값으로 반환
from numpy import nan as NA

data = Series([1, NA, 3.5, NA, 7])
data.dropna()

# 불리언 색인을 이용해 직접 계산도 가능
data[data.notnull()]

# DataFrame에서 기본적으로 NA값이 하나라도 있는 로우는 제외
data = DataFrame([[1., 6.5, 3.], [1., NA, NA], 
                  [NA, NA, NA], [NA, 6.5, 3.]])

cleaned = data.dropna()

data

cleaned

# how='all' 옵션을 주면 모든 값이 NA인 로우만 제외시킴
data.dropna(how='all')

# axis = 1을 주면 column제외
data[4] = NA
data
data.dropna(axis=1, how='all')

# 몇 개 이상의 값이 들어있는 row만 보고싶다면 thresh사용
df = DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = NA; df.ix[:2, 2] = NA
df
df.dropna(thresh=3)







