# 전역변수의 사용
# 함수 안에서 함수 밖의 변수를 사용할 때 global 키워드 사용

def sum_test():
  global a
  a = 1
  print('a:{0}'.format(a))

a = 0
sum_test()