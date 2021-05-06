#딕셔너리 {"key" : "value"} {1:"홍길동"} {오브젝트:오브젝트} => 파이썬에서 몽고DB에 값넣을때 사용
#자바스크립트 {key:value} {username : "홍길동"} {변수:"오브젝트"} => 몽고DB (자바스크립트 오브젝트를 넣어야함)
#JSON {"key":value} {"변수":오브젝트}

dic1 = {"username":"yjlee"}
print(dic1)
print("="*50)

# 값 찾기
print(dic1["username"])
print("="*50)

# 딕셔너리에 값 추가
dic1["password"] = "1234"
print(dic1)
print("="*50)

# 딕셔너리에서 값 삭제 함수 del, clear
# del 삭제

# key 값과 value 값 추출하기 (리스트형태로 출력됨)
dic2 = {"username":"yjlee","password":"1234"}
print(dic2.keys())
print("="*50)
print(dic2.values())
print("="*50)


#key값과 value값 동시에 추출하기
# for문은 들여쓰기가 끝나면 for문 종료
for i in dic2:
    print(i)

print("="*50)
#key값과 value값 동시에 추출하기

list1=[]
for k,v in dic2.items():
    print(k,v)
    list1.append(v)

print(list1)

