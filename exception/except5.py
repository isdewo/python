'''
파이썬 - 6 예외처리
p.5
str에 "점"이라는 글이 포함되어 있으므로 score를 int 타입으로 변환할 때 문제 발생
'''

str = "89점"
try:
  score = int(str)
except:
  print("예외가 발생")
else:
  print(score)