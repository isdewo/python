def var_key_args(**kwargs):
  print(type(kwargs))
  print(kwargs)

  for k, v in kwargs.items():
    print("key =", k, " value=", v)

var_key_args()
var_key_args(a=1, b=2, c=3)
