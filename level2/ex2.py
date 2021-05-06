# 클래스

class User: #클래스는 첫글자는 대문자
    username ="yjlee"
    password = "1234"


u = User() #객체생성
print(u.username)
print("="*50)


class Person:
    #생성자, 자기자신
    def __init__(self,username,password): #힙에 있는 변수 생성 및 선언
        self.username = username
        self.password = password

p=Person("yjlee","1234")
print(p.username)