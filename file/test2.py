'''
파이썬 - 7 파일 다루기
p. 19
실습 문제
'''

# 파일이름과 단어를 입력받는다.
file_name = input("파일 이름을 입력하시오: ")
word_name = input("찾을 단어를 입력하시오: ")

# 파일을 읽은후 문자를 소문자로 바꾼다.
# 찾고자 하는 단어를 찾아 count를 증가시킨다.
with open(file_name, "r") as f:
  text = f.read()
  # file의 내용 출력
  print("{} 내용\n".format(file_name), text)
  
  text = text.lower()
  pos = text.find(word_name)
  count = 0
  while pos != -1:
    count += 1
    pos = text.find(word_name, pos+1)

print("개수는 ", count)

