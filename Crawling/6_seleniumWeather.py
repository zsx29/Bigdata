"""
    날짜 : 2021-06-08
    이름 : 박재형
    내용 : 가상브러우저를 활용한 크롤링 실습
"""

from selenium import webdriver

# 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 페이지 이동
browser.get("https://www.weather.go.kr/w/obs-climate/land/city-obs.do")

# 페이지 파싱
trs = browser.find_elements_by_css_selector("#weather_table > tbody > tr")

for tr in trs:
    local = tr.find_element_by_css_selector("td:nth-child(1) > a").text
    temp = tr.find_element_by_css_selector("td:nth-child(6)").text

    print("{},{}".format(local, temp))

# 가상브라우저 종료
browser.close()
