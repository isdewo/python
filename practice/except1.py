'''
파이썬의 예외 3개를 사용하는 예제 프로그램 3개를 작성하시오.
예외
1) NameError
2) ValueError
3) ZeroDivisionError
4) IndexError
5) TypeError
'''

def input_str():
  str_list = []
  str = input("여러 개의 숫자를 띄어쓰기로 구분하여 입력해주세요: ") # ValueError
  str_list = str.split()
  for i in range(len(str_list)):
    print(int(str_list[i]), end = " ")
  return str_list

try:
  str_list = input_str()
  print(str_list[len(str_list) + 1]) # IndexError 발생
except IndexError:
  print("IndexError: 범위를 벗어났습니다.")
except ValueError:
  print("ValueError: 형식이 잘못되었습니다")
except NameError:
  print("NameError: 해당 변수가 존재하지 않습니다")
'''
finally:
  print(str_lis) # NameError 발생
'''