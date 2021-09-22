# 기본값 매개변수(default argument) 사용
# 호출시 두번째 매개변수를 생략하면 기본값 1이 사용됨


def print_hello(text, count = 1):
  for i in range(count):
    print(text)

print_hello("안녕", 3)
print("---------")
print_hello("안녕")