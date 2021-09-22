def spam(eggs):
  eggs.append(100)  # ham = [0, 100]
  eggs = [2, 3] # eggs = [2, 3]
  eggs.append(1)  # eggs = [2, 3, 1]
  print(eggs) # [2, 3, 1]

ham = [0]
spam(ham)
print(ham)  # [0, 100]