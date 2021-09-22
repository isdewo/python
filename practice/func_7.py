def calcsum(*n):
  sum = 0
  for i in n:
    sum += i
  
  return sum

print("sum = ", calcsum(1, 2, 3, 4, 5))