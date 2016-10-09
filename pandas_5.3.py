#-*- coding: utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

df = DataFrame([[1.4, np.nan], [7.1, -4.5],
                [np.nan, np.nan], [0.75, -1.3]],
                index = ['a', 'b', 'c', 'd'],
                columns=['one', 'two'])

df

# column의 합을 담은 Series반환
df.sum()

# axis=1옵션은 각 row의 합을 반환
df.sum(axis=1)

# skipna=False일 시 NA가 있는 row 또는 column은 아예 제외, 기본값은 True
df.mean(axis=1, skipna=False)

# 최대값을 갖고 있는 색인의 값(알파벳으로 표현)을 반환
df.idxmax()

# 누산 : 이전의 column 또는 row값을 누산시킴
df.cumsum()

# 한 번에 통계 결과를 여러 개 생성
df.describe()

# 수치 데이터가 아니면 다른 요약통계를 생성
obj = Series(['aa', 'bb', 'cc', 'bb'] * 4)
obj.describe()



