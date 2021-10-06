'''
파이썬 - 6 예외처리
p.8
두 개 이상의 예외 동시처리
'''
str = "89점"
try:
  score = int(str)
except (ValueError, IndexError):
  print("점수의 형식이나 첨자가 잘못됨")
else:
  print(score)
