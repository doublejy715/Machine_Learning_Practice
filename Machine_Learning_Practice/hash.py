'''
해시
1. 해시 테이블 : 딕셔너리, 객체
2. <정해진 길이의 문자열> -> 이것의 의미가 여기선 더 크다.
SHA256 <문자열> => < 정해진 길이의 문자열>
'''
import hashlib

with open("./tower.jpg","rb") as file:
    string = file.read()
    m = hashlib.md5()
    m.update(string)
    result = m.digest()
    print(result)
    """
    m = hashlib.md5()
    m.update(<문자열>)
    result = m.digest()
    """