#-*- coding: utf-8 -*-
import numpy as np

names = np.array(['Bob', 'Alice', 'Victor', 'Eve', 'Bob', 'Bob', 'Alice'])

# names들의 원소가 data배열의 row에 대응한다 가정
data = np.random.randn(7, 4)

print(names)
print(data)

# 불리언 배열이 배열의 색인으로도 사용될 수 있음 : Bob인 row가 뽑힘(총 3row)
print(data[names=='Bob'])


print("------")
# 슬라이스 색인과 혼용해서 사용
print(data[names == 'Bob', 2:])


print("NOT")
# NOT : != 또는 - 사용
print(names != 'Bob')
print(data[-(names == 'Bob')])

# OR : |
print("OR")
mask = (names=='Bob') | (names=='Alice')
print(mask)
print(data[mask])


# 값 대입 : 배열에 대입하듯이 수행하면 됨
data = np.random.randn(7, 4)
print(data)
data[data < 0] = 0
print("음수값을 0으로 대입")
print(data)

data[names != 'Eve'] = 100
print("Eve가 아닌 row의 data값을 100으로 치환")
print(data)


