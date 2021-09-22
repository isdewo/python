def calcsum(n):
  sum = 0
  for i in range(1, n+1):
    sum += i
  
  return sum

print("sum of 1 ~ 50 = ", calcsum(50))
