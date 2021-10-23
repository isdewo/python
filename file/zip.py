'''
파이썬 - 7 파일 다루기
p. 20
실습 문제
'''

import os
import zipfile

def compressZip(zipname, filename):
  print("[%s] -> [%s] 압축...." %(filename, zipname))
  with zipfile.ZipFile(zipname, 'w') as ziph:
    ziph.write(filename)

    print("압축이 끝났습니다")

def file_list():
  folder = '.'
  file_list = os.listdir(folder)
  print(file_list)
  print()

file_list() # 현재 파일 리스트를 출력한다.
filename = input("파일이름을 입력하시오: ")
zipname = filename + '.zip'
compressZip(zipname, filename)
file_list() # 압축 후 파일 리스트를 출력한다.

