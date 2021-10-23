'''
파이썬 - 7 파일 다루기
p. 10
except
'''
try:
  f = open("live.txt", "rt")
  text = f.read()
  print(text)
except FileNotFoundError:
  print("파일이 없습니다.")
finally:
  f.close()