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

# 합 구하기
frame.sum(level='key2')
frame.sum(level='color', axis=1) # 동일한 색들끼리 column단위로 더함


