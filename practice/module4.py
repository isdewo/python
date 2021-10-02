'''
x는 1, 2, 3, 4, 5로 증가하고, y는 x의 거듭제곱으로 증가한다. 
10개의 쌍 (x, y)를 원소로 가지는 리스트를 반복문을 이용하여 만드시오. 
이 리스트를 이용하여 x와 y를 plot으로 그리시오.
'''
import matplotlib.pyplot as plt

# 0~10까지 x, y에 대입
x = [i for i in range(10)]
y = []
z = []
for i in x:
  y.append(i*i)

for i in range(10):
  z.append((x[i], y[i]))

print("x = ", x)
print("y = ", y)
print("(x, y) = ", z)
plt.plot(x, y)
plt.show()