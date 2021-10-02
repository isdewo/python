'''
파이썬 -4 모듈과 패키지
p.10
'''

import random
for i in range(5):
  print(random.random()) # 난수 생성

for i in range(5):
  print(random.randint(1, 10))

for i in range(5):
  print(random.uniform(1, 10))

food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(random.choice(food))
print(random.sample(food, 2))
random.shuffle(food)
print(food)  