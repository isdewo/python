# 매개변수 전달방식
# 불변 객체를 전달 (call-by-value)
def sum(x): # x는 형식 매개변수
  x = x + 10

a = 5
sum(a)  # a는 실 매개변수

print(a) # a의 값은 변경되지 않음