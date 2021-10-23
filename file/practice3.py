'''
파이썬 - 7 파일 다루기
p. 21
연습 문제3
'''

'''
3. 파일에서 알파벳의 개수를 구하는 프로그램을 작성하시오
'''

filename = input("파일 이름을 입력하세요: ")

with open(filename, "r", encoding="utf-8") as f:
  text = f.read()
  count = 0
  for i in range(len(text)):
    if text[i].isalpha():
      # print(text[i])
      count += 1
    
  print("-----" + filename + "-----")
  print(text)
  print("알파벳의 개수는 {}개 입니다.".format(count))
