'''
파이썬 - 7 파일 다루기
p. 11
readline
'''

f = open("hello.txt", "r")
text = ""
line = 1
while True:
  row = f.readline() # 파일을 한 줄씩 읽음
  if not row: # 파일의 마지막일 때 row값은 None
    break
  text += str(line) + " : " + row
  line += 1
f.close()
print(text)