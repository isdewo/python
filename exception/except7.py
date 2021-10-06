'''
파이썬 - 6 예외처리
p.7
각 예외에 따른 처리
'''
str = "89점"
try:
  score = int(str)
except ValueError: # ValueError 예외 발생 시 수행
  print("점수의 형식이 잘못됨")
except IndexError: # IndexError 예외 발생 시 수행
  print("첨자가 범위를 벗어남")
else:
  print(score)
