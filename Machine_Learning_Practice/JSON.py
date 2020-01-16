'''
기본적으로 JSON은 []형태로 둘러싸여 있고 내부는 dict과 같은 형식으로 되어있다.
[1]JSON : 자바 스크립트 객체를 표현하기 위한 방법이다. 파이썬의 개채 표현방법과 비슷하다고 볼 수 있다.
[2]JSON 에서 사용가능한 자료형
1. 숫자 : 10,273
2. 문자열 : "(반드시 이 내에 사용한다.)"
3. 불 : true/false
4. null
5. 배열 : 파이썬과 같음 []
6. 객체 : 파이썬의 dict과 같다. { # "값" 내부에는 숫자, 문자열, 불, 배열, 객체가 사용 가능하다.
    "키A":"값",
    "키A":"값",
    "키A":"값",
    "키A":"값"
}
[3] JSON은 가장 기본적으로 []을 시작으로 한다.

'''
import json
import urllib.request as request

json_str = request.urlopen("https://api.github.com/repositories").read() # 먼저 JSON형식의 홈페이지를 들고온다.

output = json.loads(json_str) # 파이썬 형태로 다시 변환한다.
'''
print(type(output)) # list 형태로 출력이 된다.
print(output)
'''

# 내용 추출하기
for item in output:
    print(item["name"]) # 오직 key값을 통해서만 들고온다.
    print(item["full_name"])
    print(item["owner"]["login"]) # 2중 key형식은 다음과 같이 표현하여 value을 끌어온다.
    print()
'''
# JSON문자열 -> 파이썬 자료형으로 변형하고자 할 때
output = json.loads(json_str)
print(type(output))
print()
# 파이썬 자요형 -> JSON 문자열
text = json.dumps(output)
print(type(text))
'''