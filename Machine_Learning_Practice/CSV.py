# CSV(Comma-Saperated Values) : 콤마로 구분되어지는 값들
'''
항상 콤마로 구분되는것은 아니다. 띄어쓰기도 가능
[1] 규칙
1. 한 줄에 데이터 하나, 한 줄에는 쉼표로 속성 구분
2. 첫  번째 줄은 헤더로 사용 가능, 각각의 value가 어떤 의미를 지니는지 표현

[2] XML vs JSON vs CSV 의 비교
1. 같은 데이터를 가지고 표현할 때 xml의 길이가 더욱 길다. 길이 : xml > JSON > CSV
2. 표현력 : CSV = 한줄에 하나이기 때문에 매우 한정적이다, XML = 태그에 속성이나 여러가지 방법을 통해서 표현을 다양화 할 수 있다.
3. 가독성 : XML, JSON 은 코드의 중간을 보면 각 값이 어떤 것을 의미하는지 쉽게 알 수 있다. 반면 CSV는 값의 의미를 알 수 없기 때문에 가독성이 떨어진다.

최근에는 JSON이 많이 이용된다.
ID, 이름, 가격
1000,비누,300 # 1번 데이터
1001,장갑,150  # 2번 데이터
1002,마스크,230 # 3번 데이터

[3] CSV의 데이터 형성하기
주로 엑셀 파일을 통해서 만든다.
'''

# 왜 '\'를 넣을까? : \ 가 없으면 컴퓨터가 자동으로 줄바꿈 처리를 해 버린다. \을 넣게 되면 줄을 바꾸지 않겠다는 의미를 준다.
csv = """\ 
p,x,s,n,t,p,f,c,n,k,e,e,s,s,w,w,p,w,o,p,k,s,u
e,x,s,y,t,a,f,c,b,k,e,c,s,s,w,w,p,w,o,p,n,n,g
e,b,s,w,t,l,f,c,b,n,e,c,s,s,w,w,p,w,o,p,n,n,m
p,x,y,w,t,p,f,c,n,n,e,e,s,s,w,w,p,w,o,p,k,s,u
e,x,s,g,f,n,f,w,b,k,t,e,s,s,w,w,p,w,o,e,n,a,g\ 
"""
splitted = csv.split("\n") # csv를 먼저 줄바꿈을 기준으로 해서 구분하도록한다.
for item in splitted: # 줄바꿈으로 구분한것을 하나씩 넣어가면서 ','를 기준으로 구분하도록 한다.
    list_mushroom = item.split(sep = ",") # ,를 기준으로하여 각각 구분하게 된다.
    print(list_mushroom)
    # 결과로 list형식으로 단어가 하나씩 구분된 형태를 뽑아 볼 수 있다.
'''
요소 하나 선택
list_mushroom[0]
list_mushroom[1]
범위 선택
list_mushroom[1:4]
list_mushroom[5:10]
이와 같은 범위 선택을 통해서 특정 정보를 가져올 수 있다.
'''