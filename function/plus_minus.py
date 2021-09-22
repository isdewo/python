# 함수를 변수에 저장하여 호출하기

def plus(a, b):
  return a+b

def minus(a, b):
  return a-b

myfunc = [plus, minus]
print(myfunc[0](1, 2))
print(myfunc[1](1, 2))