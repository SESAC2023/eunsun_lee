import requests
from bs4 import BeautifulSoup
import pandas as pd

# 기사 목록 URL
for i in range(1,10000) :
    url = "https://www.hani.co.kr/arti/politics/list{}.html".format(i)
    #print(url)

   # 페이지 요청
    response = requests.get(url)
    html_content = response.content

    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(html_content, "html.parser")

    # 기사 링크 추출
    article_links = []
    articles = soup.find_all("h4", class_="article-title")
    for article in articles:
        link = article.a["href"]
        article_links.append(link)
    data = []
    # 각 기사의 내용 크롤링
    for link in article_links:
        # 기사 URL
        article_url = "https://www.hani.co.kr" + link

        # 페이지 요청
        article_response = requests.get(article_url)
        article_content = article_response.content

        # BeautifulSoup 객체 생성
        article_soup = BeautifulSoup(article_content, "html.parser")

        # 기사 제목
        title = article_soup.find("span", class_="title").text.strip()

        #등록날짜
        date = article_soup.find("p", class_="date-time").text.strip()
        date = date[2:13]

        # 기사 내용
        content = article_soup.find("div", class_="text").text.strip()
        reporter = content.split("\n")[-1]

        # 결과 출력

    #    print("제목:", title)
     #   print("등록날짜:", date)
      #  print("기자명:", last_line)
       # print("내용:", content)
       # print("url:", article_url)
        #print("---------------")
        data.append([title, date, content, reporter, article_links])
df = pd.DataFrame(data)
df.columns = ["title", "date", "content", "reporter", "article_links"]  # 컬럼 이름 지정
# 엑셀 파일로 내보내기
df.to_excel("articles.xlsx", index=False)

