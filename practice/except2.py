'''
파이썬의 예외 3개를 사용하는 예제 프로그램 3개를 작성하시오.
예외
1) NameError
2) ValueError
3) ZeroDivisionError
4) IndexError
5) TypeError
'''

try:
  x = int(input("0으로 나눌 숫자를 입력하세요: "))
  y = x / 0
except ZeroDivisionError as err:
  print("ZeroDivisionError: ", err)
except ValueError as err:
  print("ValueError: ", err)
except TypeError as err:
  print("TypeError: ", err)
finally:
  x = str(x)
  y = x / 0 # TypeError