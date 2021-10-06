'''
파이썬 - 6 예외처리
p.9
as 키워드로 예외 객체를 변수로 받기
'''
str = "89점"
try:
  score = int(str)
except ValueError as e:
  print(e)
else:
  print(score)
