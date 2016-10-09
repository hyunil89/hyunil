#-*- coding: utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# MultiIndex를 색인으로 하는 Series, 색인의 계층을 보여주고 있음
data = Series(np.random.randn(10), index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                                           1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])

# 바로 위 단계의 색인을 이용해 하위 계층 직접 접근 가능
data.index
data['b']
data['b':'c']
data.ix[['b', 'd']]

# 하위 게층의 객체를 선택하는 것도 가능
data[:, 2]

# unstack을 이용한 새로운 데이터 배열
data.unstack()

# unstack, stack
data.unstack().stack()

# DataFrame에서는 두 축 모두 계층적 색인 가짐
frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'],
                           ['Green', 'Red', 'Green']])
frame

frame.index.names = ['key1', 'key2']
frame.columns.names = ['stat', 'color']
frame

frame['Ohio']

# MultiIndex는 따로 생성 후에도 재사용 가능 위에것은 다음과 같이 표현 가능
MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']],
                       names=['state', 'color'])

