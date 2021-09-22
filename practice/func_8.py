def combine_string(*mystrings):
  string = ''
  for i in mystrings:
    string += i

  return string
  
print("strings = ", combine_string("Hello", "world"))