'''
파이썬 - 6 예외처리
p.12
finally 블록은 예외 발생 여부와 상관없이 반드시 실행해야 할 명령을 지정할 때 사용
'''
str = "89점"
try:
  score = int(str)
except ValueError as e:
  print(e)
else:
  print(score)
finally:
  print("무조건 수행합니다")