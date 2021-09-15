# 리스트 함축

# range(10)에 속하는 모든 정수에 대해 x^2을 계산하여 리스트 생성
a = [x ** 2 for x in range(10)]
print(a)

# range(10)에 속하는 모든 정수 중에서 짝수 리스트 생성
b = [x for x in range(10) if x % 2 == 0]
print(b)