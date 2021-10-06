'''
파이썬 - 6 예외처리
p.14
연습문제
'''
def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    print("division by zero!")
  else:
    print("result is ", result)
  finally:
    print("executing finally clause")

divide(2, 1)
divide(2, 0)
divide("2", "1")