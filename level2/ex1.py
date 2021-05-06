
# 함수 : 오버로딩 없음
# 컴파일은 순서대로

def add(a,b):
    return a+b

print(add(1,2))
print("="*50)

def minus(a, b=5):
    return a-b

print(minus(10))
print("="*50)


def many(*data): #튜플로받음
    print(data)

many(1,2,3,4,5)

def keyword(**data): #딕셔너리 데이터 받기
    print(data)

keyword(id=1, username="yjlee")


n1 = 1 #전역변수

def var_test():
    global n1 #전역변수를 함수안에서 사용하기 위해서는 global 선언을 해준다.
    n1 = 2


var_test()
print(n1)