def add(x, y, z):
  print(locals())
  return x, y, z

d = {'x': 1, 'y': 2, 'z': 3}

add(**d)