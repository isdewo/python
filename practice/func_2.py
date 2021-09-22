def var_pos_args(*args, **kwargs):
  print(type(args))
  print(args)
  print(type(kwargs))
  print(kwargs)

var_pos_args()
var_pos_args(1, 2, 3, 4)
var_pos_args(1, 2, 3, 4, a=1, b=2)
