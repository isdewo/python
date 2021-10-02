'''
파이썬 -4 모듈과 패키지
p.21
beautifulsoup4 패키지 설치 필요
'''

from urllib import request
import bs4

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=108")
soup = bs4.BeautifulSoup(target, "html.parser")
for city in soup.select("location"):
  name = city.select_one("city").string
  wf = city.select_one("wf").string
  tmn = city.select_one("tmn").string
  tmx = city.select_one("tmx").string
  print(name, ": ", wf, "(", tmn, "~", tmx, ")")
  