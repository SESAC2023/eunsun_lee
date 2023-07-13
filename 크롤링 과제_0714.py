#새싹홈페이지의 강의명과 좋아요 수 정보 가져오기

import requests
from bs4 import BeautifulSoup

# 요청(Request) 객체를 생성합니다.
request = requests.get('https://sesac.seoul.kr/course/active/online/list.do')

# 웹 사이트의 HTML 소스코드를 추출합니다.


# HTML 소스코드를 파이썬 BeautifulSoup 객체로 변환합니다.
soup = BeautifulSoup(request.text, 'html.parser')

# 특정한 클래스 이름으로 접근합니다.
data = soup.find_all('a', attrs={"class" : "sub"})
data1 = soup.find_all('div', attrs={"class" : "favor"})
for i in range(len(data)) :
    print(i+1, ".")
    print('강의명 : ', data[i].text)
    print('좋아요 수 : ', data1[i].text.strip())

