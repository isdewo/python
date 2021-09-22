# 지역변수
# 함수 내부에서만 사용되고 함수가 종료하면 사라짐

def sum_test():
  a = 1
  print('a:{0}'.format(a))

a = 0
sum_test()