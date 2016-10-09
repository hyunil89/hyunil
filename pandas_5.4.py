#-*- coding: utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# pandas는 누락된 데이터를 실수든 아니든 모두 NaN(Not a Number)로 취급
string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])

string_data
string_data.isnull()

# 파이썬의 내장 None 또한 NA로 취급
string_data[0] = None
string_data.isnull()


