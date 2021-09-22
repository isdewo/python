# 함수를 다른 함수의 매개변수로 사용하기
def print_hello():
  print('hello, python')

def greet(s):
  s()

greet(print_hello)