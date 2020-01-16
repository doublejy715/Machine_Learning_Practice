'''
어느 홈페이지에서든지 들어갈 떄는 정확하게 해당 홈페이지가 어디를 가리키고 있는지 알아야한다.(그래서 test2에서 스크린 샷을 찍은 것이다.)

'''
from selenium import webdriver
import time

url = "https://nid.naver.com/nidlogin.login"
browser = webdriver.Chrome()
browser.implicitly_wait(3)

# 여기서부터 실질적으로 원하는 작업 명령 줄을 넣어주면 된다.
browser.get(url)

id  = 'blawh945'
pw = 'de~1nf13rn0'

# Login하는 기능을 담았다.
# id,pw 둘 다 id를 통한 접근방식을 취한다.
element_id = browser.find_element_by_id("id") # id 텍스트 입력 상자를 수정 할 수 있게 된단.
element_id.clear() # 아이디 칸 지우기
time.sleep(1)
element_id.send_keys(id) # 로그인 할 아이디 내용 입력하기
time.sleep(1)

element_pw = browser.find_element_by_id("pw") # pw 텍스트 입력 상자
element_pw.clear()
time.sleep(1)
element_pw.send_keys(pw)
time.sleep(1)

# 이제 '로그인 하기'버튼을 누르도록 하자

button = browser.find_element_by_css_selector("input.btn_global[type=submit]")
button.submit() # submit 버튼이기 때문에 submit이라 칭한다.



browser.save_screenshot("Website_C.png")

# 메일페이지 열기
browser.get("https://mail.naver.com/")
browser.save_screenshot("Website_D.png")


# 이 과정을 통해서 네이버의 로그인 하는 인터넷창을 들어갈 수 있게된다.
# 또한 실제로 스크린샷을 찍어봄으로써 실제로 해당 페이지가 어떻게 구성되어있는지 확인이 가능하다.
browser.quit()

# 이제 입력을 해 준다.