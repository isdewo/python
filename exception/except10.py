'''
파이썬 - 6 예외처리
p.10
raise 명령어 사용
'''
def calsum(n):
  if(n < 0):
    raise ValueError # 예외 이름 없이 raise만 사용해도 됨
  sum = 0
  for a in range(n + 1):
    sum += a
  return sum

try:
  print(calsum(10))
  print(calsum(-5))
except:
  print("입력값이 잘못됨")
