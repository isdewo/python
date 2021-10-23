'''
파이썬 - 7 파일 다루기
p. 16
listdir 디렉터리 리스트 불러오기
'''

import os
folder = '.'
file_list = os.listdir(folder)
print(file_list)