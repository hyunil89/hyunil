#-*- coding: utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# Panel : DataFrame의 3차원 버전
from pandas_datareader import data as web

pdata = pd.Panel(dict((stk, web.get_data_yahoo(stk))
                    for stk in ['AAPL', 'GOOG', 'MSFT', 'DELL']))

pdata

pdata = pdata.swapaxes('items', 'minor')
pdata['Adj Close']

# ix를 이용한 접근 가능
pdata.ix[:, '6/1/2012', :]
pdata.ix['Adj Close', '5/22/2012':, :]

# 통계 모델에 알맞게 Panel을 출력하려면 DataFrame을 쌓아라!
stacked = pdata.ix[:, '5/30/2012':, :].to_frame()
stacked
stacked.to_panel()
stacked.to_panel.to_frame()
