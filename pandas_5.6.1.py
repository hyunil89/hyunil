#-*- coding: utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# 초보자들의 실수 : 정수 색인 시 에러 발생
ser = Series(np.arange(3.))
ser
ser[-1]

# 하지만 정수 색인이 아니라면 상관없음
# 따라서 일관성 유지를 위해 정수 데이터는 항상 이름을 지향함
ser2 = Series(np.arange(3.), index=['a', 'b', 'c'])
ser2[-1]

# iloc : 위치기반의 색인
ser3 = Series(range(3), index=[-5, 1, 3])
ser3.iloc[2]

frame = DataFrame(np.arange(6).reshape(3, 2), index=[2, 0, 1])
frame
frame.iloc[0]


