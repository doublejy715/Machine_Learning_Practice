# 해당 홈페이지에 있는 이미지 파일을 다운받아오는 코드
import urllib.request
'''
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# 다운로드

mem = urllib.request.urlopen(url).read()
 # 위 코드로 인해서 바로 png 파일로 저장하는 것이 아니라 데이터를 파이썬 위에 올릴 수  있다.


urllib.request.urlretrieve(url, savename)
위 코드를 통해서 바로 이미지 파일을 저장 가능하다.


# 이미지 파일을 저장하기
with open(savename, mode="wb") as f: # wb(write binary) : 이미지 형식으로 저장
    f.write(mem)
    print("저장되었습니다!")
'''


'''
# 텍스트 파일을 가져와서 저장하기
url = "https://www.google.co.kr/"

mem = urllib.request.urlopen(url).read()
# 여기까지 하게되면 읽어오는 것 까지 끝나게 된다.
print(mem.decode("euc-kr"))
# 프린터하게 되면 goolge main page의 소스코드를 모조리 들고 올 수 있다.

'''

# 책의 예제 따라하기
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

text = data.decode("utf-8")
print(text)