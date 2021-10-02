'''
파이썬 -4 모듈과 패키지
p.20

numpy, matplotlib 패키지 설치 필요
'''

import numpy as np
import matplotlib.pyplot as plt

# 사인 곡선에 해당하는 x와 y좌표를 계산
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# matplotlib를 사용해 점들을 표시
plt.plot(x, y)
plt.show()