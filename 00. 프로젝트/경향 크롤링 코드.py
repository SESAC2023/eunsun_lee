#자동 인코딩 감지 라이브러리 설치
pip install chardet  

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import chardet    #자동 인코딩 감지

driver = webdriver.Chrome()

# 데이터를 저장할 리스트
data = []
cnt = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


#링크 열기
url = "https://www.khan.co.kr/politics"
driver.get(url)



#페이지 로드 될때까지 기다리기
wait = WebDriverWait(driver, 10)
#wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'df-list')))

#셀레니움에서 태그 찾는 방법
# 1. 1. find_elements : element는 가장 가까운 거 하나 elements는 전부
        #예시 : driver.find_elements(By.CSS_SELECTOR, 'div[class="text"]>a')  
#2. Xpath : 셀레니움에서 경로를 이용해서 태그 찾는 방법. 정확히는 경로 표현 방법. 구성요소는 아래와 같음
        #예시는 아래 코드 참조
"""
    //: 문서 전체에서 해당 요소를 찾습니다. 즉, 모든 자식과 자손 요소를 검색합니다.
    div: div 요소를 의미합니다.
    [@class='inner']: class 속성이 "inner"인 div 요소를 선택합니다.  and를 사용하여 여러 요소 중복으로 사용 가능. 즉, class와 id 동시 조건 설정 가능
    //a: 해당 div 요소 하위의 모든 a 태그를 선택합니다.
"""
    
#기사 링크 가져오기    
article_link = []

for i in range(1,46) :
    
    #첫페이지는 a태그의 href를 이용하여 가져올 수 없음. 태그가 다름
    if i == 1 :
        
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        articles = soup.select("h2.tit>a")

        for article in articles:
            link = article['href']
            article_link.append(link)

    else :
        
#div class = "inner"  id = "paging"    a href = "javascript:listData.load(1)" 

        #위의 구조에서 javascript 부분을 이용하여 페이지 순환
        next = "javascript:listData.load({});".format(i)

        # 해당 링크를 XPath를 사용하여 요소 찾기
        page = driver.find_element(By.XPATH, "//a[@href='{}']".format(next))

        #클릭 후 기다리기
        page.click()
        wait = WebDriverWait(driver, 10)


        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        articles = soup.select("h2.tit>a")

        for article in articles:
            link = article['href']
            article_link.append(link)
#print(article_link)

#아예 다른 페이지. 이것 때문에 멈춤.
article_link.remove('https://www.khan.co.kr/politics/politics-general/article/202307190600035')


# 각 기사의 내용 스크래핑
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
for link in article_link :
    cnt += 1
    response = requests.get(link, headers=headers)
    response.encoding = 'UTF-8'   #인코딩 수동
    
    article_html_content1 = response.content
    article_soup =  BeautifulSoup(article_html_content1, 'html.parser')
    
    
    #제목
    #print(article_soup)
    title = article_soup.find("h1", class_="headline").text
    
    
    #날짜
    date = article_soup.find('div', class_="byline").text
    date = date[6:17]
    
    #기사 내용  
    content = ""
    contents = article_soup.find("div", class_="art_body", id = "articleBody").find_all("p", class_= "content_text text-l")
        if contents == [] :
            contents = article_soup.find("div", class_="art_body", id = "articleBody").find_all("p", class_= "content_text")
                
    for i in contents :
        content += i.text + " "
    
    #다른 크롤링 파일들과 똑같이 url 변수명 바꾸기
    article_url = link
    
    #기자명
    reporter = article_soup.find("span", class_="author").text
    
    
        #출력
    print(cnt)
#    print(title)
 #   print(date)
  #  print(content)
   # print(reporter)
   # print(article_url)
    #print("------------------------------------------------")
    
    
     #데이터 리스트에 추가 하여 엑셀로 내보내기
    data.append([title, date, content, reporter, article_url])    

df = pd.DataFrame(data, columns  = ["title", "date", "content", "reporter", "article_url"] )

df.to_csv("yna_articles01.csv", index=False)
