#-*- coding: utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

# unique : 중복되는 값을 제거하고 유일 값만 담은 Series반환
uniques = obj.unique()
uniques

# value_counts : Series에서 도수를 계산하여 반환, 내림차순 정렬
# pandas 최상위 메소드로 어떤 배열이나 순차 자료 구조에서도 사용 가능
obj.value_counts()
pd.value_counts(obj.values, sort=False) # sort안하고 그냥 출력

# isin : 어떤 값이 Series에 있는지 나타내는 불리언 벡터 반환
mask = obj.isin(['b', 'c'])
mask
obj[mask] # True인 것들만 반환

# 여러 로우에 대한 히스토그램 구하기
data = DataFrame({'Qu1' : [1, 3, 4, 3, 4],
                  'Qu2' : [2, 3, 1, 2, 3],
                  'Qu3' : [1, 5, 2, 4, 4]})

data

# 각 column당 1~5가 몇개나 있는지 수량조사
# 메소드의 결과가 column크기보다 작을 수 있기 때문에 fillna(0)을 통해 NA를 0으로 채움
result = data.apply(pd.value_counts).fillna(0)


