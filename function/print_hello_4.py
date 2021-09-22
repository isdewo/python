# 중첩 함수(nested function)
# 중첩 함수는 자신이 소속되어 있는 함수의 매개변수를 사용할 수 있음
# 중첩 함수는 자신이 속해있는 함수의 밖에서는 호출할 수 없음
def print_hello(s):
  def nest1():
    print(s)
    return 0
  v = nest1()
  print(v)

print_hello('hi')