'''
파이썬 - 7 파일 다루기
p. 17, 18
실습 문제
'''

import os
import random, datetime

if not os.path.isdir("log"):
  os.mkdir("log")

# 해당 파일이 존재하지 않으면 읽기 모드로 파일을 만든다.
if not os.path.exists("log/count_log.txt"):
  f = open("log/count_log.txt", "w")
  f.write("기록시작\n")
  f.close()

# 파일 내용 읽기
with open("log/count_log.txt", "r") as f:
  content = f.read()
  print(content)

# 파일에 append를 하면 그때의 날짜와 시간이 표시됨
with open("log/count_log.txt", "a") as f:
  for i in range(1, 11):
    stamp = str(datetime.datetime.now())
    value = random.random() * 1000000
    log_line = stamp + "\t" + str(value) + " 값이 생성됨" + "\n"
    f.write(log_line)

# 파일 내용을 읽어온다.
with open("log/count_log.txt", "r") as f:
  text = f.read()
  word_list = text.split(" ") # 빈 칸 기준으로 단어 분리
  line_list = text.split("\n") # 줄바꿈 기준으로 단어 분리

print("총 글자의 수: ", len(text))
print("총 단어의 수: ", len(word_list))
print("총 줄의 수: ", len(line_list))