'''
파이썬 -4 모듈과 패키지
p.9
'''

import time
t = time.time() # 1970년 이후부터 지금까지의 시간을 초로 출력

print(t)
print(time.ctime(t)) # 초를 년도, 월, 일, 요일, 시간으로 출력
print(time.localtime(t)) # struct_time 형식으로 변환 출력

start = time.time()
for a in range(100):
  print(a, end = ", ")
print()
end = time.time()
print(end - start)