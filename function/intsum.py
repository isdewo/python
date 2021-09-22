# 가변 매개변수(arbitary argument)
# 가변 매개변수는 다른 인수의 마지막에 있어야하며
# 한개만 있어야한다.

def intsum(*ints):
  sum = 0
  for s in ints:
    sum += s
  return sum

print(intsum(1, 2, 3))
print(intsum(5, 7, 9, 11, 13))