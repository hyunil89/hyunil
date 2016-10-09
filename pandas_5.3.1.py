#-*- coding: utf-8 -*-

import pandas as pd
from pandas_datareader import data

all_data={}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = data.DataReader(ticker, 'yahoo', '2015-01-01', '2016-01-01')

price = pd.DataFrame({tic: data['Adj Close'] for tic, data in all_data.items()})
volume = pd.DataFrame({tic: data['Volume'] for tic, data in all_data.items()})

returns = price.pct_change()

returns.tail()

# MSFT, IBM의 두 상관관계 계산
returns.MSFT.corr(returns.IBM)

# MSFT, IBM의 공분산 계산
returns.MSFT.cov(returns.IBM)

# 한 DataFrame의 corr, cov 계산
returns.corr()
returns.cov()

# 한 변량과 DataFrame의 모든 변량과의 corr
returns.corrwith(returns.IBM)

# 각 변량당의 변화율에 대한 상관관계, axis=1로 설정하면 변량 당이 아닌 날짜 당으로 변경
returns.corrwith(volume)







