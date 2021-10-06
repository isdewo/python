'''
파이썬의 예외 3개를 사용하는 예제 프로그램 3개를 작성하시오.
예외
1) NameError
2) ValueError
3) ZeroDivisionError
4) IndexError
5) TypeError
'''

def nameError():
  name = "이름" # 실행시 삭제할 것
  print(name)
def valueError():
  value = int("error")
def zeroDivisionError():
  y = 10 / 0
def indexError():
  error_list = ["e", "r", "r", "o", "r"]
  print(error_list[5])
def typeError():
  add = 1 + 'a'

try:
  print("1. NameError 2. ValueError 3. ZeroDivisionError 4. IndexError 5. TypeError")
  error = int(input("어떤 에러를 만들고 싶나요?? 원하는 에러의 번호를 선택하세요: "))
  if error == 1:
    nameError()
  elif error == 2:
    valueError()
  elif error == 3:
    zeroDivisionError()
  elif error == 4:
    indexError()
  elif error == 5:
    typeError()
  else:
    print("문제를 다시 읽어주세요.")
except NameError as err:
  print("NameError: ", err)
except ValueError as err:
  print("ValueError: ", err)
except ZeroDivisionError as err:
  print("ZeroDivisionError: ", err)
except IndexError as err:
  print("IndexError: ", err)
except TypeError as err:
    print("TypeError: ", err)
finally:
  print("원하는 에러를 내봤습니다.")