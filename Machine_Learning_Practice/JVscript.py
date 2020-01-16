'''
배우는 이유 : 최근에는 웹을 만들때 반드시 html만을 이용하는 것은 아니다.
최근에는 자바를 이용해서 웹을 만드는 경우가 존재한다. 이를 위해서 이것이 필요하다.
    1. Phantom JS (프로그램)
    2. Selenium (스크립트)
    이번에는 Selenium을 이용하여 보는 과정을 익힌다.
'''

from selenium import webdriver

url = "http://www.naver.com/"

# PhantomJS를 이용해서 자료를 받아오는 과정
# PhantomJS 드라이버 추출하기
browser = webdriver.Chrome()
# 3초 대기하기 wdbdriver의 버그 때문에 초기화 하기 위해서는 3초 가량 대기해야 한다.
browser.implicitly_wait(3)


# URL 읽어 들이기 : 웹브라우저에 URL을 얻어도는 과정
browser.get(url)
# 실상 여기에서 자신이 원한는 과정을 모두 넣어주면 된다.
# 화면을 캡처해서 저장하기
browser.save_screenshot("Website.png")
# 브라우저 종료하기
browser.quit()