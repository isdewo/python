'''
파이썬 - 7 파일 다루기
p. 12
writeline
'''

lines = ["we'll find a way we always have - Interstellar\n",
          "I'll find you and I'll kill you - Taken\n",
          "I'll be back - Terminator 2\n"]

with open('movie_quotes.txt', "w") as file:
  file.writelines(lines)

# movie_quotes.txt 파일 읽어오기
with open('movie_quotes.txt', "r") as file:
  line = file.readline()
  while line != '':
    print(line, end='')
    line = file.readline()