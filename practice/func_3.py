def calcstep(**args):
  begin = args['begin']
  end = args['end']
  step = args['step']

  sum = 0
  for num in range(begin, end+1, step):
    sum += num
  return sum

print("sum of 3 ~ 5 = ", calcstep(begin=3, end=5, step=1))
print("sum of 3 ~ 5 = ", calcstep(step=1, begin=3, end=5))
print("sum of 1 ~ 10 = ", calcstep(begin=1, end=10, step=2))