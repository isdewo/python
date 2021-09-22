def var_pos_args(x, y, z, *args):
  print(type(args))
  print(locals())

print(var_pos_args(1, 2, 3, 4, 5, 6))

