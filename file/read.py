'''
파이썬 - 7 파일 다루기
p. 7
read
'''
f = open("hello.txt", "r")
contents = f.read()
print(contents)
f.close()