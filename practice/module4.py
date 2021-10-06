'''
x는 1, 2, 3, 4, 5로 증가하고, y는 x의 거듭제곱으로 증가한다. 
10개의 쌍 (x, y)를 원소로 가지는 리스트를 반복문을 이용하여 만드시오. 
이 리스트를 이용하여 x와 y를 plot으로 그리시오.
'''
from math import pow
import matplotlib.pyplot as plt

# 1~10까지 x, y에 대입
x = [i for i in range(1, 11)]
y = []
z = []
for i in x:
  # y는 x의 제곱 형태로 증가
  y.append(int(pow(i, 2)))

for i in range(10):
  z.append((x[i], y[i]))

print("x = ", x)
print("y = ", y)
print("(x, y) = ", z)
plt.plot(x, y)
# plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
plt.show()