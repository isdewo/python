# 반복문
a = [1, 2, 3, 1, 2]
new_a = [] # 빈 리스트 생성

for i in a:
  if i not in new_a:
    new_a.append(i)

print(new_a)