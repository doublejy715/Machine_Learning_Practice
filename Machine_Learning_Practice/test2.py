from selenium import webdriver

# 헤드가 없는 브라우저 여는 방식
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200*600') # 스캔할 화면의 size조절하는 코드
browser = webdriver.Chrome(chrome_options=options)

url = "http://www.naver.com/"

# 보통의 헤드가 있는 브라우저
#browser = webdriver.Chrome()


browser.implicitly_wait(3)
browser.get(url)
browser.save_screenshot("Website2.png")
browser.quit()
'''
# chrome drvier를 사용하면 크게 2가지 접근방식이 가능해진다.
사용하기 위해서는 webdrivedr.Chrome() 의 형태로 작성 해 줘야한다.

# 헤드 있는 브라우저 : 화면이 나오는 상태로 조작이다.


# 헤드 없는 브라우저 : 화면이 나오지 않는 상태  -> 단순한 테스트를 위한 목적
'''