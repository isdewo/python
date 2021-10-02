'''
1부터 30까지의 서로 다른 난수 10개씩 생성하여
리스트 A와 리스트 B를 만들고,
이들의 교집합을 출력하는 프로그램을 작성하시오.
'''
import random as rand
A = []
B = []
for i in range(10):
  A.append(rand.randint(1, 30))
  B.append(rand.randint(1, 30))

print("A = ", A)
print("B = ", B)
intersection = list(set(A) & set(B))
print("A U B = ", intersection)