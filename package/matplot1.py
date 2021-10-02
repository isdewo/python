'''
파이썬 -4 모듈과 패키지
p.19

matplotlib 패키지 설치 필요
'''

import matplotlib.pyplot as plt

# 0~10까지 x, y에 대입
x = y = [i for i in range(0, 11)]
plt.plot(x, y)
plt.show()