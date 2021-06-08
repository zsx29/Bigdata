"""
    날짜 : 2021-06
    이름 : 박재형
    내용 : 영화 평점리뷰 크롤링 실습하기
"""

from selenium import webdriver

# 가상브라우저 실행
browser = webdriver.Chrome("./chromedriver.exe")

# 페이지 이동
browser.get("https://movie.naver.com/")

# 영화랭킹 클릭
btn_ranking = browser.find_element_by_css_selector("#scrollbar > div.scrollbar-box > div > div > ul > li:nth-child(3) > a")
btn_ranking.click()

# 평점순(모든영화) 클릭
btn_score = browser.find_element_by_css_selector("#old_content > div.tab_type_6 > ul > li:nth-child(3) > a")
btn_score.click()

# 평점 1위 클릭
btn_titles = browser.find_elements_by_css_selector("#old_content > table > tbody > tr > td.title > div > a")
btn_titles[0].click()

# 영화 평점 클릭
menu_score = browser.find_element_by_css_selector("#movieEndTabMenu > li:nth-child(5) > a")
menu_score.click()

# 현재 가상 브라우저를 영화리뷰가 있는 Iframe으로 전환
browser.switch_to.frame("pointAfterListIframe")

while True:
    # 영화 리뷰 출력
    lis = browser.find_elements_by_css_selector("body > div > div > div.score_result > ul > li")
    for li in lis:
        score = li.find_element_by_css_selector("div.star_score > em").text
        reple = li.find_element_by_css_selector("div.score_reple > p > span:last-child").text

        print("{},{}".format(score, reple))

    # 다음 페이지 클릭
    btn_next = browser.find_element_by_css_selector("body > div > div > div.paging > div > a:last-child")
    btn_next.click()

print("영화 리뷰 수집완료...")

















