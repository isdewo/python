'''
파이썬 - 7 파일 다루기
p. 21
연습 문제1
'''

'''
파일에서 특정 단어를 다른 단어로 교체하는 프로그램을 작성하시오.
예를 들어, "abc", "111로 대체시킴.
파일 이름과 단어 2개는 키보드로 입력받는다.
'''

filename = input("파일 이름을 입력하세요: ")
word1, word2 = input("단어 2개를 띄어쓰기로 구분하여 입력하세요: ").split(" ")

print("filename: ", filename)
print("word1: {0}, word2: {1}".format(word1, word2))

# 파일을 열어 단어를 대체함.
with open(filename, "r") as f:
  text = f.read()
  print("----- 대체 이전 -----")
  print(text)
  text = text.replace(word1, word2)
  print("----- 대체한 문장 -----")
  print(text)

# 교체된 문장을 파일에 다시 입력
with open(filename, "w") as f:
  f.write(text)

# 단어가 교체된 파일 내용 확인
print("----- 파일 내용 교체 -----")
with open(filename, "r") as f:
  text = f.read()
  print(text)
  