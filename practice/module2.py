'''
1. 1부터 100까지의 난수 10개를 생성하여 리스트를 만드시오.
리스트 원소들의 평균과 표준편차를 출력하는 프로그램을 작성하시오.
'''
import random
import statistics
rand_list = []
for i in range(10):
  rand_list.append(random.randint(1, 100))

print("리스트 원소: ", rand_list)
print("평균: ", statistics.mean(rand_list))
print("표준편차: ", statistics.stdev(rand_list))
