def rtn_tuple(a, b, c):
  return a, b, c

x, y, z = rtn_tuple(1, 2, 3)
print(x, y, z)

x, *y = rtn_tuple(1, 2, 3)
print(x, y, z)

x, *y, z = rtn_tuple(1, 2, 3)
print(x, y ,z)