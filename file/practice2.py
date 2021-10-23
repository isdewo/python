'''
파이썬 - 7 파일 다루기
p. 21
연습 문제2
'''

'''
Zip 파일의 압축을 푸는 프로그램을 작성하시오.
'''

import os
import zipfile

def decompressZip(zipname, filename):
  print("[%s] -> [%s] 압축해제" %(zipname, filename))
  with zipfile.ZipFile(zipname) as ziph:
    ziph.extractall()

    print("압축을 풀었습니다")

def file_list():
  folder = '.'
  file_list = os.listdir(folder)
  print(file_list)
  print()

file_list() # 현재 파일 리스트를 출력한다.
zipname = input("압축을 풀 파일이름을 입력하시오: ")
filename = zipname[0:len(zipname) - 4]
decompressZip(zipname, filename)
file_list() # 압축 후 파일 리스트를 출력한다.
