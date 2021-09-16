# while문
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
i = 0

while i < len(A):
  total += A[i]
  i += 1

average = total / len(A)
print(average)