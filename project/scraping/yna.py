import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
cnt = 0
# 기사 목록 URL
for i in range(1, 12) :
    url = "https://www.yna.co.kr/politics/all/{}".format(i)
   # print(url)

   # 페이지 요청
    response = requests.get(url)
    html_content = response.content

    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(html_content, "html.parser")

    # 기사 링크 추출
    article_links = []
    articles = soup.find_all("div", class_="news-con")
    #print(articles)
    for article in articles:
        link = article.a["href"]
       # print(link)
        article_links.append(link)
    
    try :
    # 각 기사의 내용 크롤링
        for link in article_links:
            # 기사 URL
            article_url = "https:" + link
            cnt += 1
            # 페이지 요청
            article_response = requests.get(article_url)
            article_content = article_response.content

            # BeautifulSoup 객체 생성
            article_soup = BeautifulSoup(article_content, "html.parser")

            # 기사 제목
            title = article_soup.find("h1", class_="tit").text.strip()

            #등록날짜
            date = article_soup.find("p", class_="update-time").text.strip()
            date = date[4:14]
            #기자
            reporters = article_soup.select("div.txt-con>strong")

            reporter = ""
            for j in reporters :
                reporter += j.text + " "
                
                
            # 기사 내용
            contents = article_soup.find("article", class_="story-news article")
            contents1 = contents.select("p:not([class])")   #클라스가 없는 p만
            #print(contents1)
            #content = content1.find_all("p")
            content = ""
            #contents = article_soup.find_all("p", class_=False)
            for i in contents1 :
                content += i.text.strip()
                content = content + " "


            #데이터 리스트에 추가 하여 엑셀로 내보내기
            data.append([title, date, content, reporter, article_url])

            # 결과 출력
            print(cnt)            
            #print("제목:", title)
            #print("등록날짜:", date)
            #print("내용:", content)
            print("기자명:", reporter)
            #print("url:", article_url)
            #print("---------------")

    except :
            pass

df = pd.DataFrame(data, columns  = ["title", "date", "content", "reporter", "article_url"] )

# 엑셀 파일로 내보내기
df.to_csv("yna_articles01.csv", index=False)
