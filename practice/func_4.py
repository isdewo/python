def add(x, y, z):
  print(locals())
  return x + y + z

t = (1, 2, 3)
print(add(*t))
print(add(t))
