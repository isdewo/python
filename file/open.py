'''
파이썬 - 7 파일 다루기
p. 8
open
'''
with open("hello.txt", "r") as f:
  content = f.read()
  print(content)

# f.close를 호출하지 않아도 파일이 닫힘