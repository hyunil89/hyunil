#-*- coding: utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'],
                           ['Green', 'Red', 'Green']])
frame

frame.index.names = ['key1', 'key2']
frame.columns.names = ['stat', 'color']
frame

# swaplevel : 넘겨받은 2개의 인덱스 위치를 swap함
frame.swaplevel('key1', 'key2')

# sortlevel : 단일 계층에 속한 데이터 정렬, 맨 앞의 인덱스를 기준으로 정렬
frame.sortlevel(1)
frame.swaplevel(0, 1).sortlevel(0)

