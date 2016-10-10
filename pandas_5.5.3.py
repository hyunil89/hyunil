#-*- coding: utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

frame = DataFrame({'a': range(7), 'b': range(7, 0, -1), 
                   'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd': [0, 1, 2, 0, 1, 2, 3]})

# set_index : 하나 이상의 칼럼을 색인으로 하는 새로운 DataFrame을 생성
# 위의 frame에서 c, d를 색인으로 하는 새로운 frame2 생성
frame2 = frame.set_index(['c', 'd'])
frame2
# 원래 c, d 값을 살리려면 drop=False
frame.set_index(['c', 'd'], drop=False)

# reset_index : set_index와 반대되는 개념으로, 계층적 색인 단계가 칼럼으로 이동
frame2.reset_index()
