import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver = webdriver.Chrome()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


#링크 열기
url = "https://www.news1.kr/categories/?1&page=100"
driver.get(url)


#페이지 로드 될때까지 기다리기
wait = WebDriverWait(driver, 10)

#셀레니움에서 태그 찾는 방법  
# 1. 1. find_elements : element는 가장 가까운 거 하나 elements는 전부
        #예시 : driver.find_elements(By.CSS_SELECTOR, 'div[class="text"]>a')  
#2. Xpath : 셀레니움에서 경로를 이용해서 태그 찾는 방법. 정확히는 경로 표현 방법. 구성요소는 아래와 같음

"""
    //: 문서 전체에서 해당 요소를 찾습니다. 즉, 모든 자식과 자손 요소를 검색합니다.
    div: div 요소를 의미합니다.
    [@class='inner']: class 속성이 "inner"인 div 요소를 선택합니다.  and를 사용하여 여러 요소 중복으로 사용 가능. 즉, class와 id 동시 조건 설정 가능
    //a: 해당 div 요소 하위의 모든 a 태그를 선택합니다.
"""
    
#기사 링크 가져오기    
article_link = []

for i in range(1, 111) :
    next = "goPage({})".format(i)

    # 해당 링크를 XPath를 사용하여 요소 찾기
    page = driver.find_element(By.XPATH, "//ul[@class='page_nav_list']//li//a[@onclick='{}']".format(next))
    #클릭 후 기다리기
    page.click()
    
    # 새로운 페이지가 로드될 때까지 기다리기
    time.sleep(1)
    #wait = WebDriverWait(driver, 10)
    #wait.until(EC.staleness_of(page))  # 클릭한 요소가 더 이상 유효하지 않을 때까지 기다림


   # articles = driver.find_elements(By.CSS_SELECTOR, "li.article a")
    articles = driver.find_elements(By.CSS_SELECTOR, "li.article a.pic_area")
    #print(articles) 
  
    for article in articles:
        link = article.get_attribute("onclick")
        link1=link[10:-2]
        article_link.append(link1) 
        #print(article)
        #print("-----------------------------------")
        #print(link1)
        
#print(article_link)  """


# 각 기사의 내용 스크래핑

#데이터 저장할 리스트
data = []
cnt = 0

for link in article_link :
    article_url = "https://www.news1.kr" + link
    cnt += 1
    response = requests.get(article_url, headers=headers)
    response.encoding = 'UTF-8'   #인코딩 수동
    
    article_html_content1 = response.content
    soup =  BeautifulSoup(article_html_content1, 'html.parser')
    
 
    #제목
    title = soup.find("div", class_="title").find("h2").text
    #print(title)

    #날짜
    info = soup.find('div', class_="info").text.split("|")
    date = info[1].strip()
    date = date[:11]
    
    #기자명
    reporter = info[0].strip()
    reporter = reporter[9:]

    #print(date)
    #print(reporter)

    #기사 내용  
    content = ""
    contents = soup.find("div", class_="detail sa_area")
    
    #print(contents)
    # <br> 태그를 기준으로 내용 분리하여 리스트에 저장
    #contents_list = contents.split('\n')
    #contents_list = [content.strip() for content in contents_list if content.strip()]
    #print(contents_list)

    #contents = contents.select("br:not([class])")   #클라스가 없는 것만
    
    for i in contents :
        content += i.text.strip()
    #print(content)

  
        #출력
    print(cnt)
    #print(title)
    #print(date)
    #print(content)
    #print(reporter)
    #print(article_url)
    #print("------------------------------------------------"))
    
    
     #데이터 리스트에 추가 하여 엑셀로 내보내기
    data.append([title, date, content, reporter, article_url])    

df = pd.DataFrame(data, columns  = ["title", "date", "content", "reporter", "article_url"] )

df.to_csv("news1_articles01.csv", index=False)
